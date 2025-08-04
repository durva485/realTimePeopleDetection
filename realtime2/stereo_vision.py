import cv2
import numpy as np

# Stereo block matcher
stereo = cv2.StereoBM_create(numDisparities=16*4, blockSize=15)

def compute_disparity_map(imgL, imgR):
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
    disparity = stereo.compute(grayL, grayR)
    return disparity
