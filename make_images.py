import numpy as np
import cv2
import os
import time

path = 'can_make_love.mp4'
movie = cv2.VideoCapture(path)
Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
out_dir = 'images/'

step = 50
print('Total frame number:', Fs)
time.sleep(1)

os.makedirs(out_dir, exist_ok=True)

width = 256
height = 256

start = 200
finish = Fs - start

count = 0
for i in range(start, finish):
    flag, frame = movie.read()
    
    if i % step == 0:
    
        print()
        print('--progress {} frame --'.format(count))
        
        if flag:
            out_path = out_dir + '%06d.png' % count
            img = cv2.resize(frame, (height, width))
            cv2.imwrite(out_path, img)
            count += 1
