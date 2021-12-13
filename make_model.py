# -*- coding: utf-8 -*-
import h5py
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os
from utils.vgg_net import VGGNet
# model = VGG16(weights='imagenet', include_top=False)
#
# img_path = '1.jpg'
# img = image.load_img(img_path, target_size=(224, 224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
#
# features = model.predict(x)
def get_imlist(path):
    file_list = []
    dir_list = os.listdir(os.path.join(path))
    for f in dir_list:
        new_file = path+'/'+f
        file_list.append(new_file)
        pass
    image_file_list = []
    for img in file_list:
        img_path = os.listdir(img)
        for ii in img_path:
            new_img_path = img+'/'+ii
            image_file_list.append(new_img_path)
    # print(image_file_list)
    return image_file_list



    # return [ for f in os.listdir(path) if f.endswith('.jpg')]


if __name__ == '__main__':
    # ll =os.listdir(os.path.join('JingManCang/101010_综合工具套装'))
    # res = get_imlist('JingManCang')
    # print(res)

    # database = 'database'
    database = 'JingManCang'
    index = 'models/vgg_featureCNN.h5'
    img_list = get_imlist(database)
    print("_______________________________________")
    print("________feature extraction starts____________")
    print("_______________________________________")

    feats = []
    names = []
    model = VGGNet()
    for i,img_path in enumerate(img_list):
        norm_feat = model.vgg_extract_feat(img_path)
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        print("extracting feature from image No.%d, %d images in total"%((i+1),len(img_list)))
    feats = np.array(feats)
    output = index
    print("_______________________________________")
    print("________writing feature extraction results____________")
    print("_______________________________________")

    h5f = h5py.File(output,'w')
    h5f.create_dataset('dataset_1',data=feats)
    h5f.create_dataset('dataset_2',data=np.string_(names))
    h5f.close()




















