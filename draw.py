import cv2
import numpy as np

from predictions import find_contours, get_predictions



drawing = False # true if mouse is pressed
ix,iy = -1,-1
# mouse callback function
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),5,(255,255,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),5,(255,255,255),-1)     

# initialize the main window parameters
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Window')
cv2.setMouseCallback('Window',draw)

# load our main window
while True:
    cv2.imshow('Window',img)
    k = cv2.waitKey(1)&0xFF

    if k==27: # 27 means esc key
        break
    elif k==13: # 13 means enter key 
        # [it's not necessary in this project, but] convert the main image to gray scale  
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        # Blur image    
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        contours = find_contours(blurred)
        preds = get_predictions(blurred, contours)

        result = "The number is: " + ''.join(preds)
        cv2.putText(img, result, (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 0), 1)
        cv2.imshow('Window', img)
        break


    # break


cv2.waitKey()
cv2.destroyAllWindows()


