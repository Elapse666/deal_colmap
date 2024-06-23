from read_write_model import *
import numpy as np


# a = np.loadtxt("images.txt")
# print(a.shape)

# 想办法从一堆信息中提取自己需要的信息

# # /home/ousunlight/projects/My_demo/colmap_test/images_bicycle.bin
# # /home/ousunlight/projects/My_demo/colmap_test/images_outside.bin
# images = read_images_binary('/home/ousunlight/projects/My_demo/colmap_test/images_outside.bin')
# # /home/ousunlight/projects/My_demo/colmap_test/images_bicycle.txt
# # /home/ousunlight/projects/My_demo/colmap_test/images_outside.txt
# image_path = '/home/ousunlight/projects/My_demo/colmap_test/images_outside.txt'
# write_images_text(images, image_path)



file = open ("images_bicycle.txt", "r", encoding = "UTF-8")
file = file.readlines()

original_list = []

for line in file:
    # print(line)
    temp = line.strip().split()
    # print(temp)
    # print(len(temp))
    

    if(len(temp) == 10):
        # print(type(temp[0]))
        # print(temp[0])
        del temp[9]
        del temp[8]
        del temp[0]
        original_list.append(temp)
        

del original_list[1]
del original_list[0]

print(original_list)
print(len(original_list))



b = np.array(original_list, dtype = float)
np.savetxt("images_bicycle_deal.txt", b, fmt='%.18f')


