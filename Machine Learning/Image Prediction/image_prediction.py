'''
There are 4 different algorithms and model types:
    MobileNetV2
    ResNet50 # from Microsoft
    InceptionV3 # from Google
    DenseNet121 # from Facebook
'''

from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd() # get the pwd (present working directory)

prediction = ImageClassification()
prediction.setModelTypeAsResNet50() # 1
prediction.setModelPath(os.path.join(execution_path, 'resnet50_imagenet_tf.2.0.h5')) # 2
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, 'giraffe.jpg'), result_count = 5) # 3
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , ' : ' , eachProbability)

'''
1: choose 1 of the 4 different algorithms
2: download the model and type the name (model_name.h5) depending on the choice of the algorithm
3: change the image name to see predictions and probabilities

Important: place image_prediction.py, model_name.h5 and image_name.jpg in the same directory
'''
