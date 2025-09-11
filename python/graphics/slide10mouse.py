import cv2
import numpy as np

canvas = np.zeros((800,200,3),dtype=np.uint8)
color = ""
def mouse_callback(event,x,y,flags,params):
    global color

    if event == cv2.EVENT_LBUTTONDOWN:
        if color == "yellow":
            green = 0
            red = 255
            color = "red"
        elif color == "green":
            green = 255
            red = 255
            color = "yellow"
        elif color == "red":
            green = 255
            red = 0
            color = "green"
        else:
            green = 255
            red = 0
            color = "green"
        cv2.circle(canvas,center=(100,400),radius=50,color=(0,green,red),thickness=-1)
        cv2.imshow("Canvas",canvas)

def main():
    global color
    cv2.imshow("Canvas",canvas)
    cv2.setMouseCallback('Canvas',mouse_callback)
    
    while True:

        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            cv2.circle(canvas,center=(100,400),radius=50,color=(0,0,255),thickness=-1)
            color = "red"
            cv2.imshow("Canvas",canvas)

        elif key == ord('y'):
            cv2.circle(canvas,center=(100,400),radius=50,color=(0,255,255),thickness=-1)
            cv2.imshow("Canvas",canvas)
            color = "yellow"

        elif key == ord('g'):
            cv2.circle(canvas,center=(100,400),radius=50,color=(0,255,0),thickness=-1)
            cv2.imshow("Canvas",canvas)
            color = "green"

        elif key == 27:
            break
        
    cv2.destroyAllWindows()

main()