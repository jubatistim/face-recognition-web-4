from custom_util_test import *
import cv2

# img = cv2.imread('test-files/01.jpg')

# image_predicted = predict_Luna_Ju(img)

# cv2.imshow('pred' , image_predicted)
# cv2.waitKey(0)

for i in range(1,21):
    img = cv2.imread('test-files/a (' + str(i) + ').jpg')

    image_predicted = predict_Luna_Ju(img)

    cv2.imshow('pred' + str(i), image_predicted)
    cv2.waitKey(0)