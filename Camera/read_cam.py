import numpy as np

calib = "redmi.txt"
calib = np.loadtxt(calib, delimiter=" ")
print(calib)
print(calib.shape)
fx, fy, cx, cy = calib[:4]
print(fx)