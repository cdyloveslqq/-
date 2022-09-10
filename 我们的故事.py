import numpy as np
import cv2
import pygame
cap = cv2.VideoCapture('D:\一生的许诺\image\一生的许诺.mp4')

while (cap.isOpened()):

    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

pygame.init()
pygame.mixer.music.load("D:\CloudMusic\凯瑟喵 - 撒野.mp3")
pygame.mixer.music.play(-1, start=139)
pygame.mixer.music.set_volume(0.5)
cap.release()
cv2.destroyAllWindows()
