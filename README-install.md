```shell
conda install cudatoolkit==10.1.243 -y
pip install  torch==1.8.1 torchvision
wget https://download.openmmlab.com/mmcv/dist/1.3.5/torch1.8.0/cu101/mmcv_full-latest%2Btorch1.8.0%2Bcu101-cp37-cp37m-manylinux1_x86_64.whl
pip install mmcv...

pip install -e .
```

#### train
```shell
python tools/train.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco_jewelry.py
```
#### test and inference
```shell
python tools/test.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco_jewelry.py work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/latest.pth --eval bbox segm
```
####inference
```shell
python tools/inference.py \
--checkpoint=work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/latest.pth \
--config=configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco_jewelry.py \
--img=demo/j2/微信图片_20210602110032.jpg
```
