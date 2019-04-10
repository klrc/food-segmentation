import tensorflow as tf
from tensorflow.python.platform import gfile

GRAPH_PB_PATH = '.pb/mask_rcnn_shapes_1250.pb'  # path to your .pb file
with tf.Session() as sess:
    with gfile.FastGFile(GRAPH_PB_PATH, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
        for i, n in enumerate(graph_def.node):
            print("Name of the node - %s" % n.name)
    g = sess.graph

    writer = tf.summary.FileWriter("logs/", g)

    import cv2 as cv
    import numpy as np

    src = cv.imread("/home/sh/github/food-segmentation/testimg.png")
    src = np.array(src, dtype=float)
    src = np.reshape(src, [1, 128, 128, 3])
    input_image = tf.placeholder(shape=[None, None, 3], dtype=tf.float16, name="input_image")
    input_anchors = tf.placeholder(shape=[None, 4], dtype=tf.float32, name="input_anchors")
    input_image_meta = tf.placeholder(shape=[43], dtype=tf.float16, name="input_image_meta")

    import json

    with open('.pb/input_anchor.json', 'r') as f:
        anchors = json.load(f)
        anchors = np.array(anchors, dtype=float)
        anchors = np.reshape(anchors, [1, 4092, 4])

    meta = [0, 128, 128, 3, 128, 128, 3, 0, 0, 128, 128, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    meta = np.array(meta, dtype=float)
    meta = np.reshape(meta, [1, 43])

    output = g.get_operation_by_name('output_2')

    print(input_image.shape, src.shape)
    print(input_anchors.shape, anchors.shape)
    print(input_image_meta.shape, meta.shape)

    result = sess.run(output, feed_dict={input_image: src, input_anchors: anchors, input_image_meta: meta})
    # print(result)
