import cv2
import numpy as np
import random
import torch
from coco_names import COCO_INSTANCE_CATEGORY_NAMES as coco_names
from coco_names import COCO_INSTANCE_CATEGORY_COLORS_DICT as coco_colors
from scipy import ndimage

def get_outputs(image, model, threshold, depth_frame):
    with torch.no_grad():
        # forward pass of the image through the modle
        outputs = model(image)
    
    # get all the scores
    scores = list(outputs[0]['scores'].detach().cpu().numpy())
    # index of those scores which are above a certain threshold
    thresholded_preds_inidices = [scores.index(i) for i in scores if i > threshold]
    thresholded_preds_count = len(thresholded_preds_inidices)
    # get the masks
    masks = (outputs[0]['masks']>0.5).squeeze().detach().cpu().numpy()
    # discard masks for objects which are below threshold
    masks = masks[:thresholded_preds_count]
    # get the bounding boxes, in (x1, y1), (x2, y2) format
    boxes = [[(int(i[0]), int(i[1])), (int(i[2]), int(i[3]))]  for i in outputs[0]['boxes'].detach().cpu()]
    # discard bounding boxes below threshold value
    boxes = boxes[:thresholded_preds_count]
    # get the center of masks
    cvtMasks = [masks[i].astype(int) for i in range(len(masks))]
    centers = [ndimage.center_of_mass(c) for c in cvtMasks]
    centers = np.array(centers).astype(int)
    # get the classes labels
    labels = [coco_names[i] for i in outputs[0]['labels']]
    # get the depth of masks
    # print(depth_frame.shape, masks[0].shape)
    depths_mm = [np.mean(depth_frame[masks[i]==True]) for i in range(len(masks))]

    return masks, boxes, labels, centers, depths_mm

def get_Velocity(time, cur, last):
    # print(time)
    if len(cur) != 0:
        v = [np.round((cur[i]-last[i])/time*0.001, decimals=2) for i in range(len(cur))]
        return v
    return 0

def draw_segmentation_map(image, masks, boxes, labels, centers, depths_mm, velocity, loc):
    alpha = 1 
    beta = 0.6 # transparency for the segmentation map
    gamma = 0 # scalar added to each sum
    rows, cols, chan = image.shape
    cX_image = cols//2
    for i in range(len(masks)):
        # select color by label
        color = coco_colors[labels[i]]
        # draw masks
        mask_img = np.zeros_like(image)
        mask_img[masks[i] == 1] = color
        # get depth
        depth_mm = depths_mm[i]
        # get velocity
        v = velocity[i]
        # get location
        locX, locY, _ = loc[i]
        locX = np.round(locX*1000, 3)
        locY = np.round(locY*1000, 3)
        #convert the original PIL image into NumPy format
        image = np.array(image)
        # convert from RGN to OpenCV BGR format
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # draw centroid
        coord_x, coord_y = centers[i]
        cv2.circle(image, (coord_y, coord_x), 20, (0,0,255), -1)
        # apply mask on the image
        cv2.addWeighted(image, alpha, mask_img, beta, gamma, image)
        # draw the bounding boxes around the objects
        cv2.rectangle(image, boxes[i][0], boxes[i][1], color=color, 
                      thickness=2)
        
        # put the label text above the objects
        cv2.putText(image , labels[i], (boxes[i][0][0], boxes[i][0][1]-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(image, "{} cm".format(depth_mm / 10), (boxes[i][0][0], boxes[i][0][1]+40), 
                    0, 1.0, color, 2)
        # put velocity
        cv2.putText(image, "{} m/s".format(v), (boxes[i][0][0], boxes[i][0][1]+160), 
                    0, 1.0, color, 2)
        # put locations
        cv2.putText(image, "X: {} m".format(locX), (boxes[i][0][0], boxes[i][0][1]+80), 
                    0, 1.0, color, 2)
        cv2.putText(image, "Y: {} m".format(locY), (boxes[i][0][0], boxes[i][0][1]+120), 
                    0, 1.0, color, 2)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

