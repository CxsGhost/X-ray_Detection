import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET

path = r'./VOC2007/JPEGImages'  # 原文件夹路径
newpath = r'./VOC2007/Annotations'  # 新文件夹路径
# c_w, c_h = 600, 600  # 全黑画布的大小
data_y = []


def edit_xml(xml_file):
    """
    修改xml文件
    :param xml_file:xml文件的路径
    :return:
    """
    all_xml_file = os.path.join(newpath, xml_file)
    print(xml_file)
    tree = ET.parse(all_xml_file)
    objs = tree.findall('object')
    the_number = 0
    for ix, obj in enumerate(objs):
        if obj.find('name').text == '气孔':
            the_number += 1
    data_y.append(the_number)



if __name__ == '__main__':
    files = os.listdir(path)
    print(files)  # 获取文件名列表
    for i, file in enumerate(files):
        if file.endswith('.jpg'):
            imgName = os.path.join(path, file)  # 获取文件完整路径
            xml_file = file.replace('.jpg', '.xml')
            edit_xml(xml_file)
    data_y = np.array(data_y)
    print(data_y)
    np.save('./data_y.npy', data_y)

            # img = cv2.imread(imgName, )  # 读图
            # h, w, _ = img.shape  # 获取图像宽高
            # # 缩放图像，宽高大于800的按长边等比例缩放，小于800的保持原图像大小：
            # if max(w, h) > c_w:
            #     ratio = c_w / max(w, h)
            #     imgcrop = cv2.resize(img, (round(w * ratio), round(h * ratio)))
            #     # 将裁切后的图像复制进全黑图像里
            #     img_zeros[0:round(h * ratio), 0:round(w * ratio)] = imgcrop
            #     edit_xml(xml_file, ratio, i)
            # else:
            #     img_zeros[0:h, 0:w] = img
            #     edit_xml(xml_file, 1, i)
            #
            # # 设置新的文件名：
            # newName = os.path.join(path, file)
            # print(newName)
            # cv2.imwrite(newName, img_zeros)  # 存储按新文件名命令的图片
