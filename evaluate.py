import os
import glob
import time
import argparse

# Kerasa / TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model
from layers import BilinearUpSampling2D
from loss import depth_loss_function
from utils import predict, load_images, display_images, evaluate
from matplotlib import pyplot as plt


# Custom object needed for inference and training
from model import DepthEstimate
# Load model into GPU / CPU
print('Loading model...')
model= DepthEstimate()
import tensorflow
from loss import depth_loss_function
batch_size     = 16

learning_rate  = 0.0001
epochs         = 1
optimizer = tensorflow.keras.optimizers.Adam(lr=learning_rate, amsgrad=True)
model.load_weights("training_1/cp.ckpt")
model.compile(loss=depth_loss_function, optimizer=optimizer)

# Load test data
print('Loading test data...', end='')
import numpy as np
from data import extract_zip
data = extract_zip('nyu_test.zip')
from io import BytesIO
rgb = np.load(BytesIO(data['eigen_test_rgb.npy']))
depth = np.load(BytesIO(data['eigen_test_depth.npy']))
crop = np.load(BytesIO(data['eigen_test_crop.npy']))
print('Test data loaded.\n')
from skimage.transform import resize
rgb1=[]
depth1=[]
for i in range(len(rgb)):
    rgb1.append(resize(rgb[i], (224,224), preserve_range=True, mode='reflect', anti_aliasing=True ))
for j in range(len(depth)):
    depth1.append(resize(depth[j], (112,112), preserve_range=True, mode='reflect', anti_aliasing=True ))
start = time.time()
print(np.shape(rgb1))
print(np.shape(depth1))
print('Testing...')
e = evaluate(model, rgb1, depth1, crop, batch_size=6)

print("{:>10}, {:>10}, {:>10}, {:>10}, {:>10}, {:>10}".format('a1', 'a2', 'a3', 'rel', 'rms', 'log_10'))
print("{:10.4f}, {:10.4f}, {:10.4f}, {:10.4f}, {:10.4f}, {:10.4f}".format(e[0],e[1],e[2],e[3],e[4],e[5]))

end = time.time()
print('\nTest time', end-start, 's')
