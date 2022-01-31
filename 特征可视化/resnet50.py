#%%

from tensorflow import keras
from tensorflow.keras import Input, layers, models, preprocessing
from tensorflow.keras.applications import ResNet50V2
import numpy as np
import os
import cv2
# gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
# for gpu in gpus:
#     tf.config.experimental.set_memory_growth(gpu, True)


# data_x = []
# files = os.listdir('./VOC2007/JPEGImages/')
# for f in files:
#     img = preprocessing.image.load_img('./VOC2007/JPEGImages/' + f, target_size=(640, 640, 3))
#     img = preprocessing.image.img_to_array(img)
#     data_x.append(img)
# data_y = np.load('./data_y.npy')
# data_x = np.array(data_x)
# model_0 = ResNet50V2(include_top=False,
#                      weights='imagenet',
#                      input_shape=(640, 640, 3))
#
# the_input = Input(shape=(640, 640, 3))
# x = model_0(the_input)
# x = layers.Flatten()(x)
# x = layers.Dense(512, activation='relu')(x)
# output = layers.Dense(1)(x)
#
# the_model = models.Model(inputs=[the_input], outputs=[output])
# print(the_model.summary())
# the_model.compile(optimizer='Adam',
#                   loss='mse')
# the_model.fit(data_x, data_y,
#               epochs=20,
#               batch_size=2,
#               verbose=1)
#
#
#
# #%%
# conv2_out = model_0.get_layer('conv3_block1_preact_relu').output
# conv3_out = model_0.get_layer('conv4_block1_preact_relu').output
# conv4_out = model_0.get_layer('conv5_block1_preact_relu').output
# conv5_out = model_0.get_layer('post_relu').output
# fea_model = keras.Model(inputs=[model_0.input], outputs=[conv2_out, conv3_out, conv4_out, conv5_out])
# #%%
#
#
# def cope_out(out_img, name_):
#     out_img = keras.backend.squeeze(out_img, 0)
#     out_img = np.sum(out_img, axis=-1)
#     out_img = keras.backend.expand_dims(out_img, 2)
#     out_img = out_img / np.max(out_img) * 255
#     out_img = np.rint(out_img).astype('uint8')
#     # plt.imshow(out_img, )
#     # plt.show()
#     cv2.imwrite(name_, out_img)
#
# #%%
# path = './VOC2007-640'
# def save_fea_map(path_):
#     conv2_path = os.path.join(path_, 'conv2')
#     conv3_path = os.path.join(path_, 'conv3')
#     conv4_path = os.path.join(path_, 'conv4')
#     conv5_path = os.path.join(path_, 'conv5')
#     ori_path = os.path.join(path_, 'img_dete')
#     files = os.listdir(ori_path)
#     for img_name in files:
#         img_name = img_name
#         img_path = os.path.join(ori_path, img_name)
#         img = keras.preprocessing.image.load_img(img_path, target_size=(640, 640, 3))
#         img = keras.preprocessing.image.img_to_array(img)
#         img = keras.backend.expand_dims(img, axis=0)
#         out = fea_model(img)
#         cope_out(out[0], os.path.join(conv2_path, img_name))
#         cope_out(out[1], os.path.join(conv3_path, img_name))
#         cope_out(out[2], os.path.join(conv4_path, img_name))
#         cope_out(out[3], os.path.join(conv5_path, img_name))
#         break
# save_fea_map(path)
import matplotlib.pyplot as plt

def show_fea_img(img_path):
    img = keras.preprocessing.image.load_img(img_path, target_size=(640, 640, 1))
    img = keras.preprocessing.image.img_to_array(img)[:, :, 0]
    plt.imshow(img.astype('uint8'))
    plt.show()
show_fea_img('E:\py\基于X光图的工业焊缝缺陷检测系统\特征可视化/results\conv4\W0003_0029_3440_640_640.jpg')