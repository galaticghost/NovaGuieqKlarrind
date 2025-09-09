import cv2
import numpy as np

canvas = cv2.imread("atitus1.png")

img_height,img_width,channels = canvas.shape

A = ""
T = ""
I = ""

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(canvas, f"{x},{y}", (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', canvas)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        b, g, r = canvas[y, x]
        cv2.putText(canvas, f"{b},{g},{r}", (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', canvas)

cv2.imshow("image",canvas)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()