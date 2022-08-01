import cv2
import numpy as np
from os.path import exists

from tensorflow.keras.models import load_model

import train
from preprocessors import x_cord_contour, makeSquare, resize_to_pixel

def find_contours(img):
    """ This function finds contours of the given image"""

    # Find edges by using Canny
    edged = cv2.Canny(img, 30, 150)

    # Find Contours
    contours, _= cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Sort out contours left to right by using their x cordinates
    contours = sorted(contours, key = x_cord_contour, reverse = False)

    return contours

def get_predictions(img, contours):
    """This Functions get predictions from our model."""

    #Load the model, if it is not available, train the model.
    model_exists = exists('mnist_cnn.h5')
    if model_exists:
        classifier = load_model('mnist_cnn.h5')
    else:
        train.run()
        classifier = load_model('mnist_cnn.h5')

    # Create empty array to store entire number
    full_number = []

    # loop over the contours
    for c in contours:
        # compute the bounding box for the rectangle
        (x, y, w, h) = cv2.boundingRect(c)    
        
        # preprocess the image
        if w >= 5 and h >= 25:
            roi = img[y:y + h, x:x + w]
            ret, roi = cv2.threshold(roi, 127, 255,cv2.THRESH_BINARY)
            roi = makeSquare(roi)
            roi = resize_to_pixel(28, roi)
            # cv2.imshow("ROI", roi)
            roi = roi / 255.0       
            roi = roi.reshape(1,28,28,1) 

            ## Get Prediction
            result = str(np.argmax(classifier.predict(roi, 1, verbose = 0)))
                
            # Update full_number array
            full_number.append(result)

            # Add rectangle and prediction for each digit in main window
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.putText(img, result, (x , y + 155), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)
            cv2.imshow('Window', img)
            cv2.waitKey()

    return full_number

            

    
            #         cv2.destroyAllWindows()
