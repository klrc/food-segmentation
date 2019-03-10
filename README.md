# Mask R-CNN for food segmentation
(origin repo says:)
This is an implementation of [Mask R-CNN](https://arxiv.org/abs/1703.06870) on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.

# Getting Started
* [preprocessing.py](preprocessing.py) generates the .feeder dir from your own dataset, which contains resized images divided into train/test. To have a quick start:
  
        data_list = [x for x in scan_data(
            '/run/media/sh/My Passport/erkeyiyuan/数据/网络/netfood', # change these lines with your own dataset.
            '/run/media/sh/My Passport/erkeyiyuan/数据/本地菜品/压缩包')]

* [core.py](core.py) if the .feeder dir is generated, and make sure the path to 'mask_rcnn_coco.h5' is set, you can do whatever you want with core.py.
  
        # Directory to save logs and trained model
        MODEL_DIR = '.logs'

        # Local path to trained weights file
        COCO_MODEL_PATH = 'mask_rcnn_coco.h5'
        # Download COCO trained weights from Releases if needed
        if not os.path.exists(COCO_MODEL_PATH):
            utils.download_trained_weights(COCO_MODEL_PATH)

        # count = len(imglist)  # 文件的数目
        IMG_WIDTH = 200
        IMG_HEIGHT = 150
   

