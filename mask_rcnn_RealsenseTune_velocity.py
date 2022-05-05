import torch
import torchvision
import cv2
import argparse
from PIL import Image
from utils_velocity import *
from torchvision.transforms import transforms as transforms
from realsense_camera import *
import time

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

curr_depth = []
last_depth = []

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
    masks, boxes, labels, centers, depths_mm = get_outputs(image, model, 0.965, depth_frame)
    # print(centers)
    # get location of centers
    loc = rs.get_Point_Loc(centers)
    # get the velocity of each masked obj
    new_frame_time = time.time()
    timeStep = new_frame_time-prev_frame_time

    curr_depth = depths_mm
    if len(last_depth)==0:
        last_depth = np.zeros_like(curr_depth)

    velocity = get_Velocity(timeStep, curr_depth, last_depth)
    # draw results on the image
    result = draw_segmentation_map(orig_image, masks, boxes, labels, centers, depths_mm, velocity, loc)
    
    # Calculating the fps
    fps = 1/timeStep
    # print(fps)
    # converting the fps into integer
    fps = np.round(fps).astype(int)*4
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
    prev_frame_time = new_frame_time
    last_depth = curr_depth

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(result, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    # visualize the image
    cv2.imshow('D435i', result)

    c = cv2.waitKey(1)
    if c == 27:
        break