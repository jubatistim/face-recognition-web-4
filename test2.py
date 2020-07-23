import os
import cv2
import numpy as np
import sys
from keras.models import load_model
from keras.preprocessing import image as image_utils

# get running path
base_dir = os.path.dirname(__file__)

model = load_model(os.path.join(base_dir, 'saved-models', 'cnn1595292938.h5'))

for filename in os.listdir('./test-files/justface'):

    img = cv2.imread('./test-files/justface/' + filename)

    img = cv2.resize(img, (64, 64), interpolation = cv2.INTER_AREA)

    img = image_utils.img_to_array(img)/255.
    
    img = np.expand_dims(img, axis = 0)

    # np.set_printoptions(threshold=sys.maxsize)
    # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    # with open('out.txt', 'w') as f:
    #     print('Filename:', img, file=f)  # Python 3.x
    # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    # break

    result = model.predict(img)

    print(type(result))
    print(result.shape)