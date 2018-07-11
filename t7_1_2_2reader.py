# -*- coding: utf-8 -*-
"""
@author: tz_zs

读取TFRecord文件中的数据
"""
import tensorflow as tf

reader = tf.TFRecordReader()
filename_queue = tf.train.string_input_producer(["/path/to/output.tfrecords"])
_, serialized_example = reader.read(filename_queue)

features = tf.parse_single_example(serialized_example,
                                   features={
                                       'pixels': tf.FixedLenFeature([], tf.int64),
                                       'label': tf.FixedLenFeature([], tf.int64),
                                       'image_raw': tf.FixedLenFeature([], tf.string)
                                   })

# tf.decode_raw 可以将字符串解析成图相对应的像素数组
images = tf.decode_raw(features['image_raw'], tf.uint8)
labels = tf.cast(features['label'], tf.int32)
pixels = tf.cast(features['pixels'], tf.int32)

sess = tf.Session()
#  启动多线程处理输入数据
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

# 每次运行读取一个样例
for i in range(10):
    image, label, pixel = sess.run([images, labels, pixels])
    print(image)
    print(label)
    print(pixel)
    break

'''
[  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0  97  96  77 118  61   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0  90 138 235 235 235 235 235
 235 251 251 248 254 245 235 190  21   0   0   0   0   0   0   0   0   0
   0   0 140 251 254 254 254 254 254 254 254 254 254 254 254 254 254 254
 189  23   0   0   0   0   0   0   0   0   0   0 226 254 208 199 199 199
 199 139  61  61  61  61  61 128 222 254 254 189  21   0   0   0   0   0
   0   0   0   0  38  82  13   0   0   0   0   0   0   0   0   0   0   0
  34 213 254 254 115   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0  84 254 254 234   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0  84 254 254 234   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0 106 157 254 254 243  51
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  25
 117 228 228 228 253 254 254 254 254 240   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0  68 119 220 254 254 254 254 254 254 254 254
 254 142   0   0   0   0   0   0   0   0   0   0   0   0   0  37 187 253
 254 254 254 223 206 206  75  68 215 254 254 117   0   0   0   0   0   0
   0   0   0   0   0   0 113 219 254 242 227 115  89  31   0   0   0   0
 200 254 241  41   0   0   0   0   0   0   0   0   0   0   0   0 169 254
 176  62   0   0   0   0   0   0   0  48 231 254 234   0   0   0   0   0
   0   0   0   0   0   0   0   0  18 124   0   0   0   0   0   0   0   0
   0  84 254 254 166   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0 139 254 238  57   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0 210 250 254 168   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0 242 254 239  57   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0  89 251 241  86   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   5 206 246 157   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   4 117  69   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0   0   0   0   0   0   0   0   0]
7
784

'''
