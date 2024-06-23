# import sys
# sys.path.append('/home/ousunlight/projects/My_demo/colmap_test')

# from .. import read_write_model
# from .. import colmap_loader
# from .. import datasets_readers
from read_write_model import *
# from colmap_loader import *
# from datasets_readers import *
# import numpy as np
# if __name__ == '__main__':
#     images = read_images_binary('/home/ousunlight/projects/My_demo/colmap_test/0/images.bin')
 
#     if len(images) == 0:
#         mean_observations = 0
#     else:
#         mean_observations = sum((len(img.point3D_ids) for _, img in images.items()))/len(images)
#     HEADER = "# Image list with two lines of data per image:\n" + \
#              "#   IMAGE_ID, QW, QX, QY, QZ, TX, TY, TZ, CAMERA_ID, NAME\n" + \
#              "#   POINTS2D[] as (X, Y, POINT3D_ID)\n" + \
#              "# Number of images: {}, mean observations per image: {}\n".format(len(images), mean_observations)
 
#     with open('/home/ousunlight/projects/My_demo/colmap_test/images.txt', "w") as fid:
#         fid.write(HEADER)
#         for _, img in images.items():
#             image_header = [img.id, *img.qvec, *img.tvec, img.camera_id, img.name]
#             first_line = " ".join(map(str, image_header))
#             fid.write(first_line + "\n")

# 
'''
    结合博客, 写出了这个脚本, 可以直接在终端运行, 也可以直接在pycharm中运行,
    但是需要注意的是, 需要在pycharm中设置环境变量, 否则会报错。
    1. 读取模型文件，得到所有的图像、点云、相机信息
    2. 将图像、点云、相机信息写入到txt文件中
    官方给的脚本确实很香
    bin -> txt      txt -> bin 都有对应的代码直接用
'''

# images = read_images_binary('/home/ousunlight/projects/My_demo/colmap_test/0/images.bin')
# image_path = '/home/ousunlight/projects/My_demo/colmap_test/images.txt'
# points3D = read_points3D_binary('/home/ousunlight/projects/My_demo/colmap_test/0/points3D.bin')
# Point3D_path = '/home/ousunlight/projects/My_demo/colmap_test/points3D.txt'
# cameras = read_cameras_binary('/home/ousunlight/projects/My_demo/colmap_test/0/cameras.bin')
# cameras_path = "/home/ousunlight/projects/My_demo/colmap_test/cameras.txt"


# write_images_text(images, image_path)
# write_points3D_text(points3D, Point3D_path)
# write_cameras_text(cameras, cameras_path)

# 设定要读取的pose bin文件

image_bin_dir = "/home/ousunlight/projects/pre-restruction/car/lab_car/images.bin"
intrinsics_bin_dir = "/home/ousunlight/projects/pre-restruction/car/lab_car/cameras.bin"
ouput_pose_txt = "/home/ousunlight/projects/pre-restruction/car/pose_bin2txt_lab_car.txt"

images = read_images_binary(image_bin_dir)
intrinsics = read_intrinsics_binary(intrinsics_bin_dir)

# 设定要生成的 pose txt文件
# pose_est_path = ouput_pose_txt
# write_poses_text(images, pose_est_path)

print(images)
print(intrinsics[1])    # 有意思    intrinsics[cam_id]

# idx类似于索引， key相当于字典dict中的索引
for idx, key in enumerate(images):
    print(idx)
    print(key)