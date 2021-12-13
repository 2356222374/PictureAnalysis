# -*- coding: utf-8 -*-
import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from utils.vgg_net import VGGNet
# query = 'test.jpg'
# query = 'test1.jpg'
# query = '55.jpg'
# query = '99.jpg'
# query = 'ygp2.jpg'
# query = '666.jpg'
query = '777.png'
index = 'models/vgg_featureCNN.h5'
result = 'database'

h5f = h5py.File(index,'r')
feats = h5f['dataset_1'][:]
imgNames = h5f['dataset_2'][:]
h5f.close()
print("_______________________________________")
print("________searching starts____________")
print("_______________________________________")

#read and show qurey image
queryImg = mpimg.imread(query)
plt.title("Query Image")
plt.imshow(queryImg)
plt.show()

#init VGGNet16 model
model = VGGNet()
queryVec = model.vgg_extract_feat(query)#修改此处改变提取特征的网络
scores = np.dot(queryVec,feats.T)
rank_ID = np.argsort(scores)[::-1]
rank_score = scores[rank_ID]

#number of top retrieved images to show
maxres = 3 #检索出三张相似度最高的图片
imlist = []
for i,index in enumerate(rank_ID[0:maxres]):
    imlist.append(imgNames[index])
    print("image names:"+str(imgNames[index]) + "scores:%f"%rank_score[i])
print("top %d images in order are:"%maxres,imlist)
for i,im in enumerate(imlist):
    image = mpimg.imread(result +"/"+str(im,'utf-8'))
    plt.title("search output %d"%(i+1))
    plt.imshow(image)
    plt.show()