# coding=utf-8
import cv2
import numpy as np

def add_wm(img_path, wm_path, transformer_path):
    img = cv2.imread(img_path)
    img_fft = np.fft.fft2(img)
    wm = cv2.imread(wm_path)

    img_height, img_width = img.shape[0], img.shape[1]
    wm_height, wm_width = wm.shape[0], wm.shape[1]

    tmp = np.zeros(img.shape)

    for m in range(img_height):
        for n in range(img_width):
            if m < wm_height and n < wm_width:
                tmp[m][n] = wm[m][n]

    transformer_fft = img_fft + tmp
    transformer = np.fft.ifft2(transformer_fft)
    transformer = np.real(transformer)

    cv2.imwrite(transformer_path, transformer)

def get_wm(img_path, transformer_path, wm_path):
    img = cv2.imread(img_path)
    img_fft = np.fft.fft2(img)

    transformer = cv2.imread(transformer_path)
    transformer_fft = np.fft.fft2(transformer)

    wm = transformer_fft - img_fft
    wm = np.real(wm)

    cv2.imwrite(wm_path, wm)