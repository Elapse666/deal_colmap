from read_write_model import *
from colmap_loader import *
from datasets_readers import *
import numpy as np
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


# a = np.loadtxt("images.txt")
# print(a.shape)


# images = read_images_binary('/home/ousunlight/projects/My_demo/colmap_test/images_bicycle.bin')
# pose_est_path = '/home/ousunlight/projects/My_demo/colmap_test/pose_est_bicycle.txt'
# write_poses_text(images, pose_est_path)


path = "/home/ousunlight/projects/My_demo/colmap_test"
# image_bin_dir = "/home/ousunlight/projects/My_demo/colmap_test/0/images.bin"
cameras_extrinsic_file = os.path.join(path, "0", "images.bin")
cameras_intrinsic_file = os.path.join(path, "0", "cameras.bin")
cam_extrinsics = read_extrinsics_binary(cameras_extrinsic_file)
cam_intrinsics = read_intrinsics_binary(cameras_intrinsic_file)
print(cam_extrinsics)
print(cam_intrinsics)

cam_infos_unsorted = readColmapCameras(cam_extrinsics=cam_extrinsics, cam_intrinsics=cam_intrinsics, images_folder=os.path.join(path, reading_dir))
cam_infos = sorted(cam_infos_unsorted.copy(), key = lambda x : x.image_name)

# 定义保存文件的路径
file_path = 'YYQ_cam_infos.txt'

# 打开文件，以写入模式打开（'w'）
with open(file_path, 'w') as file:
    # 遍历字典中的键值对，并将其写入文件中
    for key, value in cam_infos.items():
        file.write(f'{key}: {value}\n')