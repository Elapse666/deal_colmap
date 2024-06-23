from tqdm import tqdm
import numpy as np
import torch
import cv2
import os
import glob 
import time
import argparse

import evo      # 导入evo包，用于计算数据集相关信息
from evo.core.trajectory import PoseTrajectory3D    
from evo.tools import file_interface    
from evo.core import sync               
import evo.main_ape as main_ape         
from evo.core.metrics import PoseRelation       

'''
    这个文件专门用于评估tum数据集和ETH3D数据集
    关于EuRoc数据集, 还需要再看看               --24.1.7
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--datapath", help="根目录")
    # parser.add_argument("--traj_path")
    # parser.add_argument("--imagedir", type=str, help="path to image directory")
    parser.add_argument("--traj_est", type=str, help="path to calibration file")
    parser.add_argument("--traj_gt", type=str, help="path to calibration file")
    args = parser.parse_args()

    stride = 1
    # 获取数据集图像路径 ETH3D len is 1180
    image_path = os.path.join(args.datapath, 'rgb')     # 不如直接传入根目录
    images_list = sorted(glob.glob(os.path.join(image_path, '*.png')))[::stride]
    # print(f"the list len is {len(images_list)}")
    # 时间轴必须要获取
    tstamps = [float(x.split('/')[-1][:-4]) for x in images_list]
    
    # 获取数据集路径
    traj_est = np.loadtxt(args.traj_est, delimiter=" ")              # 读取视觉里程计
    traj_ref = file_interface.read_tum_trajectory_file(args.traj_gt) # 读取TUM数据集GT
    # print(f"traj_ref shape = {np.array(traj_ref).shape}")
    # 他会导出相对应的数据,会转化成一个特定的格式,但是这个格式怎么才能转换回去呢/
    traj_est = PoseTrajectory3D(
        positions_xyz=traj_est[:,:3],   # 前三个数据
        orientations_quat_wxyz=traj_est[:,3:],  # 四元数
        timestamps=np.array(tstamps))
    
    # 轨迹对齐？
    traj_ref, traj_est = sync.associate_trajectories(traj_ref, traj_est)    

    result = main_ape.ape(traj_ref, traj_est, est_name='traj', 
        pose_relation=PoseRelation.translation_part, align=True, correct_scale=True)
    # 打印
    print(result.stats)
    print(result)
    
    # 将对齐好的数据保存在对应的文件里面
    # 将对齐的数据保存为np格式
    est_points_aligned = np.array(traj_est.positions_xyz)
    est_quat_aligned = np.array(traj_est.orientations_quat_wxyz)
    gt_points_aligned  = np.array(traj_ref.positions_xyz)
    gt_quat_aligned  = np.array(traj_ref.orientations_quat_wxyz)
    est_aligned = np.concatenate((est_points_aligned, est_quat_aligned), axis=1) # 在这里拼接xyz和四元数
    gt_aligned = np.concatenate((gt_points_aligned, gt_quat_aligned), axis=1)
    est_str = args.traj_est.split('/')[-1].split('.')[0]   # 截取 traj_est/ETH3D_traj_est.txt ----> ETH3D_traj_est_aligned.txt
    gt_str = args.traj_gt.split('/')[-1].split('.')[0]
    # 其实只要前三个位置元素，但是合并一下也无所谓
    np.savetxt('./traj_est_aligned/'+ est_str + '_aligned' +'.txt', est_aligned, fmt='%.3f')
    np.savetxt('./traj_gt_aligned/'+ gt_str + '_aligned' +'.txt', gt_aligned, fmt='%.3f')
