import cv2
import numpy as np

canvas = np.zeros((600,800,3),dtype=np.uint8)
color = (255,0,0)
shape = "rectangle"
thickness = 1

x1 = x2 = y1 = y2 = 0

def mouse_callback(event,x,y,flags,param):
    global x1,x2,y1,y2
    global shape
    global thickness

    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y

    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y

    if event == cv2.EVENT_RBUTTONDOWN:
        if shape == "rectangle":
            shape = "line"
        elif shape == "line":
            shape = "circle"
        else:
            shape = "rectangle"
    
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0: 
            thickness += 1
        else:         
            if thickness > -1: 
                thickness -= 1
                print(thickness)
        if thickness == 0:
            thickness = 1

def main():
    global color
    global x1,x2,y1,y2
    global shape
    global thickness

    cv2.imshow("Canvas",canvas)
    cv2.setMouseCallback('Canvas',mouse_callback)
    
    while True:
        cv2.rectangle(canvas,(620,520),(800,590),color=(0,0,0),thickness=-1)
        cv2.putText(canvas,shape,(641,556),cv2.FONT_HERSHEY_SIMPLEX,1,color=(255,255,255),thickness=2)
        if x1 and x2 and y1 and y2:
            if shape == "rectangle":
                cv2.rectangle(canvas,(x1,y1),(x2,y2),color,thickness)
            elif shape == "line":
                cv2.line(canvas,(x1,y1),(x2,y2),color,thickness)
            else: # TODO
                raiz = np.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
                radius = int(raiz)
                cv2.circle(canvas,(x1,y1),radius=radius,color=color,thickness=thickness)
            x1 = x2 = y1 = y2 = 0
        cv2.imshow("Canvas",canvas)
        key = cv2.waitKey(1) & 0xFF
        match(key):
            case 27:
                break
            case 49:
                color = (255,0,0)
            case 50:
                color = (0,255,255)
            case 51:
                color = (0,255,0)
            case 52:
                color = (0,0,255)
            case _:
                continue
        
    cv2.destroyAllWindows()

main()