import os
import shutil


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

def copy_to_other(filelist):
    for index,files in enumerate(filelist):
        filename1 = str(files).split("/")[-1] # 读取文件后缀名
        # filename0 = os.path.splitext(files)[0]  #读取文件名
        # if filename1 == ".jpg" :
        shutil.copy(files,"database"+"/"+filename1)
        if filename1:
            print("成功复制：",filename1)
        else:
            print("复制完成！")
        pass
           # 需要将files改为绝对路径

if __name__ == '__main__':
    list_ = get_imlist('JingManCang')
    res = copy_to_other(list_)
    print(res)
    pass