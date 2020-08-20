# face-recognition-web-4

[![Build status](https://dev.azure.com/jubatistim/face-recognition-web-4/_apis/build/status/face-recognition-web-4-Docker%20container-CI)](https://dev.azure.com/jubatistim/face-recognition-web-4/_build/latest?definitionId=9)

CNN model trained in with tensorflow and keras in Python 3.7

Trained with samples images of Ju and Luna that were generated using OpenCV to identify faces in photos.

The model was deployed in a flask app with a simple web interface, that get faces from input image, process the image in the model, show recognition results and presents the % of confidence.
