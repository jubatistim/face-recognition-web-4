from custom_util_test import *
import cv2
from keras.preprocessing import image

# img = cv2.imread('test-files/01.jpg')

# image_predicted = predict_Luna_Ju(img)

# cv2.imshow('pred' , image_predicted)
# cv2.waitKey(0)

for i in range(1,21):
    img = cv2.imread('test-files/a (' + str(i) + ').jpg')

    image_predicted = predict_Luna_Ju(img)

    cv2.imshow('pred' + str(i), image_predicted)
    cv2.waitKey(0)


# test_image_luna = image.load_img('D:\\NR\\data\\live2013\\caps.bmp', target_size=(64,64))
# test_image2 = image.img_to_array(test_image_luna)/255.
# test_image2 = np.expand_dims(test_image2, axis=0)
# luna = classifier.predict_proba(test_image2)