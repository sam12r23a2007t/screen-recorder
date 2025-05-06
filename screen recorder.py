from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 12.0, (width, heigth))

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, heigth))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen recoder', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
