import numpy as np

'''
    npy保存方法
    np.save('a.npy', a)
    np.save('b.npy', b)
    # npy 转换 txt 的方法
    np.savetxt('car_est_droid.txt', traj_est, fmt='%.18e')
    # npy 文件读取
    data1 = np.load('a.npy')
'''


# npy 文件读取

''' 这段代码主要是检测 DROID 得到的 npy 文件'''

disps_npy_dir = '/home/ousunlight/projects/DROID-SLAM/reconstructions/lab_car/disps.npy'
images_noy_dir = '/home/ousunlight/projects/DROID-SLAM/reconstructions/lab_car/images.npy'
intrins_npy_dir = '/home/ousunlight/projects/DROID-SLAM/reconstructions/lab_car/intrinsics.npy'
pose_npy_dir = '/home/ousunlight/projects/DROID-SLAM/reconstructions/lab_car/poses.npy'
tstamps_npy_dir = '/home/ousunlight/projects/DROID-SLAM/reconstructions/lab_car/tstamps.npy'

# 逆深度
disps = np.load(disps_npy_dir)
# 每一张图片，每一个像素点的RGB信息 (106, 3, 328, 584) 106张图片，height、width = 328, 584
images = np.load(images_noy_dir)
# [69.32257  69.15287  37.126575 21.013025]
intrins = np.load(intrins_npy_dir)
pose = np.load(pose_npy_dir)
tstamps = np.load(tstamps_npy_dir)

# print(images)
print(disps)
print(disps.shape)
print(len(disps))
# np.savetxt('labcar_images_droid.txt', pose, fmt='%.18e')

