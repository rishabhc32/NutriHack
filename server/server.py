from flask import Flask
from werkzeug import FileStorage
from flask import request
from flask import Response

import numpy as np

import pandas as pd

import tensorflow as tf

from ast import literal_eval

import keras

from keras import layers

from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
import cv2
from keras.models import Model, load_model

from keras.models import Sequential

from keras.models import model_from_json

app = Flask(__name__)

def prediction(x):
    img = cv2.imread(x)
    img = cv2.resize(img, (100,100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.reshape([1,100,100,1])

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model_weights.h5")

    print("Loaded model from disk")

    loaded_model.compile(loss=keras.losses.categorical_crossentropy, optimizer='adam',metrics=['accuracy'])

    pred =  loaded_model.predict(img,steps=1)

    if((np.argmax(pred)+1) == 1):
        return 'samosa'
    elif((np.argmax(pred)+1) == 2):
        return 'kachori'
    elif((np.argmax(pred)+1) == 3):
        return 'aloo_paratha'
    elif((np.argmax(pred)+1) == 4):
        return 'idli'
    elif((np.argmax(pred)+1) == 5):
        return 'jalebi'

@app.route('/nutrihack_api', methods=['POST','GET'])
def nutrihack_api():
    FileStorage(stream=request.files['nutrient_info']).save('image.jpg')

    snack = prediction('image.jpg')
    print(snack)

    #resp = Response(snack, mimetype='text/plain')
    #resp.headers['Access-Control-Allow-Origin'] = '*'
    #resp.headers['Access-Control-Allow-Headers'] = 'text/plain'

    return snack
