# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
'''
@File     :   .py
@Time     :   2021/03/08 17:09:54
@Author   :   Y.L.Xie
@Function :   截取视频帧
'''
import cv2
import os
def video2frame(videos_path, frames_save_path,  star_min, star_sec, end_min, end_sec, time_interval):
    '''
    :param videos_path: 视频的存放路径
    :param frames_save_path: 视频切分成帧之后图片的保存路径
    :param time_interval: 保存间隔
    :return:
    '''
    vidcap = cv2.VideoCapture(videos_path)
    FPS = vidcap.get(cv2.CAP_PROP_FPS)  # 获取帧率单位帧每秒
    print("视频帧率为:", FPS)
    timeStame = int((star_min*60+star_sec)*FPS)  # 视频从timeStame开始
    print("视频从{}帧开始:".format(timeStame))
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, timeStame)  # 设置开始帧率
    success, image = vidcap.read()

    count = 0
    file_name = 1

    time_frame = int(((end_min * 60 + end_sec) - (star_min * 60 + star_sec) )* FPS /time_interval) #一共应该截取的图片数量
    print("一共截取的图片数量:", time_frame)

    while success and file_name <= time_frame:
        success, image = vidcap.read()
        count += 1
        if count % time_interval == 0:
            cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "%.6d.jpg" % file_name)
            print("file_name:", file_name)
            file_name += 1

if __name__ == '__main__':

    star_min = 0 #开始 分
    star_sec = 0 #开始 秒
    end_min = 39
    end_sec = 30
    time_interval = 30  # 隔"time_interval"帧保存一次
    #视频路径
    videos_path = "F:\\code6_medicine_seg\\6医学图像数据and标注数据\\视频\\湘雅视频4_liuronghua_妙手\\M_07182018044039_00000000U1824014_2_001_0001-01.MP4"
    #帧保存路径
    frames_save_path = "F:\\image-processing\\image1-video-to-images\\" + "湘雅视频3_刘荣华0008-01_妙手_" + str(star_min) + "min_to_" + str(end_min) + "min_" + "time_interval"+str(time_interval)+"\\"

    if not os.path.exists(frames_save_path):
        os.makedirs(frames_save_path)  # 创建新文件夹

    video2frame(videos_path, frames_save_path, star_min, star_sec, end_min, end_sec, time_interval)