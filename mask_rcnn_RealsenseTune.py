import torch
import torchvision
import cv2
import argparse
from PIL import Image
from utils import *
from torchvision.transforms import transforms as transforms
from realsense_camera import *
import time
import numpy as np

rs = RealsenseCamera()

# initialize the model
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True, progress=True, 
                                                           num_classes=91)
# set the computation device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
# load the modle on to the computation device and set to eval mode
model.to(device).eval()

# transform to convert the image to tensor
transform = transforms.Compose([
    transforms.ToTensor()
])


# used to record the time when we processed last frame
prev_frame_time = 0
# used to record the time at which we processed current frame
new_frame_time = 0

while True:
    ret, frame, depth_frame = rs.get_frame_stream()
    # for webcame
    # ret, frame = cap.read()
    # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    image = frame
    orig_image = image.copy()
    # transform the image
    image = transform(image)
    # add a batch dimension
    image = image.unsqueeze(0).to(device)
    # apply model to prediction
    masks, boxes, labels, centers = get_outputs(image, model, 0.965)
    # get location of centers
    loc = rs.get_Point_Loc(centers)
    # for i in range(len(labels)):
    #     print(labels[i],loc[i])
    print(loc)
    # draw results on the images
    result = draw_segmentation_map(orig_image, masks, boxes, labels, centers, depth_frame, loc)

    new_frame_time = time.time()
    # Calculating the fps
 
    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    # converting the fps into integer
    fps = np.round(fps)
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
    cv2.putText(result, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 3, cv2.LINE_AA)

    # visualize the image
    # imS = cv2.resize(result, (1980, 1080))
    cv2.imshow('D435i', result)

    c = cv2.waitKey(1)
    if c == 27:
        break