COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]
# COLORS = np.random.uniform(0, 255, size=(len(coco_names), 3)).astype(np.uint8)
COCO_INSTANCE_CATEGORY_COLORS =[
    [211, 110, 83],[193, 33, 194],[225, 184, 169],[36, 131, 32],[166, 34, 108],[246, 195, 59],[149, 89, 25],[30, 56, 191],[79, 19, 183],
    [67, 202, 248],[155, 93, 117],[154, 179, 74],[217, 38, 121],[61, 162, 164],[202, 254, 6],[16, 138, 88],[25, 248, 33],[208, 140, 61],
    [253, 168, 254],[82, 162, 181],[140, 226, 57],[4, 34, 90],[187, 50, 21],[24, 200, 131],[222, 246, 72],[135, 58, 106],[80, 56, 195],
    [180, 242, 163],[141, 74, 38],[71, 210, 155],[75, 46, 76],[120, 243, 94],[177, 66, 230],[19, 70, 67],[83, 64, 87],[9, 76, 214],[73, 94, 186],
    [153, 10, 112],[88, 58, 19],[25, 3, 57],[93, 127, 164],[75, 139, 117],[241, 60, 73],[183, 0, 177],[101, 127, 131],[159, 199, 19],
    [76, 226, 96],[54, 4, 45],[145, 111, 232],[39, 217, 201],[237, 18, 49],[34, 114, 217],[127, 159, 182],[189, 7, 26],[10, 201, 88],
    [67, 128, 216],[199, 167, 60],[220, 109, 221],[58, 72, 38],[90, 195, 132],[76, 228, 92],[139, 99, 108],[188, 12, 19],[242, 166, 6],
    [3, 52, 170],[198, 242, 75],[87, 138, 50],[86, 4, 178],[146, 95, 61],[70, 126, 34],[0, 90, 157],[91, 214, 99],[43, 44, 107],[151, 223, 170],
    [91, 222, 170],[240, 15, 72],[90, 72, 3],[81, 229, 9],[126, 221, 9],[45, 19, 120],[148, 158, 30],[166, 221, 227],[154, 184, 102],
    [17, 215, 174],[177, 113, 158],[0, 100, 74],[250, 229, 32],[116, 95, 247],[82, 232, 7],[160, 115, 176]
 ]
# print(len(COCO_INSTANCE_CATEGORY_COLORS))
# COCO_INSTANCE_CATEGORY_COLORS_DICT = dict(zip(COCO_INSTANCE_CATEGORY_NAMES, COCO_INSTANCE_CATEGORY_COLORS))
COCO_INSTANCE_CATEGORY_COLORS_DICT = {'__background__': [211, 110, 83], 'person': [193, 33, 194], 'bicycle': [225, 184, 169], 'car': [36, 131, 32], 'motorcycle': [166, 34, 108], 'airplane': [246, 195, 59], 'bus': [149, 89, 25], 'train': [30, 56, 191], 'truck': [79, 19, 183], 'boat': [67, 202, 248], 'traffic light': [155, 93, 
117], 'fire hydrant': [154, 179, 74], 'N/A': [154, 184, 102], 'stop sign': [61, 162, 164], 'parking meter': [202, 254, 6], 'bench': [16, 138, 88], 'bird': [25, 248, 33], 'cat': [208, 140, 61], 'dog': [253, 168, 254], 'horse': [82, 162, 181], 'sheep': [140, 226, 57], 'cow': [4, 34, 90], 'elephant': [187, 50, 21], 'bear': [24, 200, 131], 'zebra': [222, 246, 72], 'giraffe': [135, 58, 106], 'backpack': [180, 242, 163], 'umbrella': [141, 74, 38], 'handbag': [120, 243, 94], 'tie': [177, 66, 230], 'suitcase': [19, 70, 67], 'frisbee': [83, 64, 87], 'skis': [9, 76, 214], 'snowboard': [73, 94, 186], 'sports ball': [153, 10, 112], 'kite': [88, 58, 19], 'baseball bat': [25, 3, 57], 'baseball glove': [93, 127, 164], 'skateboard': [75, 139, 117], 'surfboard': [241, 60, 73], 'tennis racket': [183, 0, 177], 'bottle': [101, 127, 131], 'wine glass': [76, 226, 96], 'cup': [54, 4, 45], 'fork': [145, 111, 232], 'knife': [39, 217, 201], 'spoon': [237, 18, 49], 'bowl': [34, 114, 217], 'banana': [127, 159, 182], 'apple': [189, 7, 26], 'sandwich': [10, 201, 88], 'orange': [67, 128, 216], 'broccoli': [199, 167, 60], 'carrot': [220, 109, 221], 'hot dog': [58, 72, 38], 
'pizza': [90, 195, 132], 'donut': [76, 228, 92], 'cake': [139, 99, 108], 'chair': [188, 12, 19], 'couch': [242, 166, 6], 'potted plant': [3, 52, 
170], 'bed': [198, 242, 75], 'dining table': [86, 4, 178], 'toilet': [0, 90, 157], 'tv': [91, 214, 99], 'laptop': [43, 44, 107], 'mouse': [151, 223, 170], 'remote': [91, 222, 170], 'keyboard': [240, 15, 72], 'cell phone': [90, 72, 3], 'microwave': [81, 229, 9], 'oven': [126, 221, 9], 'toaster': [45, 19, 120], 'sink': [148, 158, 30], 'refrigerator': [166, 221, 227], 'book': [17, 215, 174], 'clock': [177, 113, 158], 'vase': [0, 100, 
74], 'scissors': [250, 229, 32], 'teddy bear': [116, 95, 247], 'hair drier': [82, 232, 7], 'toothbrush': [160, 115, 176]}
# print(COCO_INSTANCE_CATEGORY_COLORS_DICT['person'])
# print(COCO_INSTANCE_CATEGORY_COLORS_DICT)
