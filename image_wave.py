# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:46:07 2017

@author: Konada

Python Version : 3.5
"""

import numpy as np
import cv2

if __name__ == '__main__':
    
    size = 512, 512, 3
    original_img = np.zeros(size, dtype=np.uint8)
    original_img2 = np.zeros(size, dtype=np.uint8)
        
    waveLength = 512 / 2
    
    print("test")

    for w in range(int(waveLength)):
        pixel = int(255.0 / waveLength * w)
        pixel2 = int(255.0 / (waveLength * waveLength) * w * w)
        
        for h in range(512):
            original_img[h, w, 0]  = pixel
            original_img[h, w, 1]  = pixel
            original_img[h, w, 2]  = pixel
            original_img2[h, w, 0]  = pixel2
            original_img2[h, w, 1]  = pixel2
            original_img2[h, w, 2]  = pixel2

            original_img[h, 511 - w, 0]  = pixel
            original_img[h, 511 - w, 1]  = pixel
            original_img[h, 511 - w, 2]  = pixel
            original_img2[h, 511 - w, 0]  = pixel2
            original_img2[h, 511 - w, 1]  = pixel2
            original_img2[h, 511 - w, 2]  = pixel2
            
    cv2.imwrite("test.bmp", original_img)
    cv2.imwrite("test2.bmp", original_img2)

    cv2.waitKey(0)