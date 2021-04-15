import os
import pandas as pd
from pycocotools.coco import COCO

work_dirs = './work_dirs/faster_rcnn_r50_fpn_1x_trash'

epoch = 12

prediction_strings = []
file_names = []
coco = COCO('../data/private_data.json')
output = pd.read_pickle(os.path.join(work_dirs, f'epoch_{epoch}.pkl'))
imag_ids = coco.getImgIds()

for i, out in enumerate(output):
    prediction_string = ''
    image_info = coco.loadImgs(coco.getImgIds(imgIds=i))[0]
    for j in range(11):
        for o in out[j]:
            prediction_string += str(j) + ' ' + str(o[4]) + ' ' + str(o[0]) + ' ' + str(o[1]) + ' ' + str(
                o[2]) + ' ' + str(o[3]) + ' '

    prediction_strings.append(prediction_string)
    file_names.append(image_info['file_name'])

submission = pd.DataFrame()
submission['PredictionString'] = prediction_strings
submission['image_id'] = file_names
submission.to_csv(os.path.join(work_dirs, f'submission_{epoch}.csv'), index=None)
print(submission.head())