## Install
1. `conda install pytorch=1.7.0 cudatoolkit=10.1 torchvision -c pytorch`

2. `pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.7.0/index.html`

3. `pip install -r requirements/build.txt`

4. `pip install -v -e .`

## notebook
### train
[faster_rcnn_train.ipynb](https://github.com/Pstage-Segmentation-Detection/mmdetection_trash/blob/master/faster_rcnn_train.ipynb)
### inference
[faster_rcnn_inference.ipynb](https://github.com/Pstage-Segmentation-Detection/mmdetection_trash/blob/master/faster_rcnn_inference.ipynb)

## python
### train
`python tools/train.py configs/trash/faster_rcnn/faster_rcnn_r50_fpn_1x_trash.py`
### inference
`python tools/test.py configs/trash/faster_rcnn/faster_rcnn_r50_fpn_1x_trash.py work_dirs/faster_rcnn_r50_fpn_1x_trash/epoch_12.pth --out work_dirs/faster_rcnn_r50_fpn_1x_trash/epoch_12.pkl`
### make submission
`python pkl_to_submission.py`