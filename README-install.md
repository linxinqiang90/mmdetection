```shell
conda install cudatoolkit==10.1.243 -y
pip install  torch==1.8.1 torchvision
wget https://download.openmmlab.com/mmcv/dist/1.3.5/torch1.8.0/cu101/mmcv_full-latest%2Btorch1.8.0%2Bcu101-cp37-cp37m-manylinux1_x86_64.whl
pip install mmcv...

pip install -e .
```

#### train
```shell
python tools/train.py configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco_jewelry.py --resume-from work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/lastest.pth
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
```shell
python tools/inference_dir.py \
--checkpoint=work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/latest.pth \
--config=configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco_jewelry.py \
--img=demo/test --score-thr 0.8 \
--checkpoint work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/epoch_769.pth 

```

####analysis
```shell
python tools/analysis_tools/analyze_logs.py plot_curve work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/20210610_102332.log.json --keys loss_cls  --legend loss_cls
```

####tensorboard
```shell
pip install future tensorboard
tensorboard --logdir=work_dirs/faster_rcnn_r50_fpn_1x_coco_jewelry/tf_logs
#filter regex
^(val|train)/loss$
```

####loss
- oss_bbox    
一种损失，衡量模型在真实物体周围预测的边界盒的“紧密”程度（通常是回归损失，L1，smoothL1等等。）。 
- loss_cls    
衡量正确性的损失
