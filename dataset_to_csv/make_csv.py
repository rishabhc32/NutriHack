import cv2               # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm
import csv
import pandas as pd
TRAIN_DIR ='train_images'
TEST_DIR= 'test_images'
IMG_SIZE=28
def label_img(img):
    word = img.split("(")[-2]
    if word=='samosa ': return [1,0,0,0,0,0,0,0,0,0]
    elif word=='kachori ': return [0,1,0,0,0,0,0,0,0,0]
    elif word=='aloo_paratha ': return [0,0,1,0,0,0,0,0,0,0]
    elif word=='idli ': return [0,0,0,1,0,0,0,0,0,0]
    elif word=='jalebi ': return [0,0,0,0,1,0,0,0,0,0]
    elif word=='tea ': return [0,0,0,0,0,1,0,0,0,0]
    elif word=='paneer_tikka ': return [0,0,0,0,0,0,1,0,0,0]
    elif word=='dosa ': return [0,0,0,0,0,0,0,1,0,0]
    elif word=='omlet ': return [0,0,0,0,0,0,0,0,1,0]
    elif word=='poha ': return [0,0,0,0,0,0,0,0,0,1]
    
def load_train_data(snacks,i):
    images = []
    labels = []
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        word = img.split("(")[-2]
        if word == snacks:
            label = label_img(img)
            path = os.path.join(TRAIN_DIR,img)
            img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
            images.append(img.tolist())
            labels.append(label)
    df = pd.DataFrame({'images':images,'labels':labels})
    stri = 'train_data' + str(i) + '.csv'
    df.to_csv(stri,index=False)
    return training_data

def load_test_data():
    testing_data = []
    snacks = ['samosa ','kachori ','aloo_paratha ','idli ','jalebi ']
    for img in tqdm(os.listdir(TEST_DIR)):
        word = img.split("(")[-2]
        if word in snacks:
            label = label_img(img)
            path = os.path.join(TEST_DIR,img)
            img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
            testing_data.append([np.array(img),np.array(label)])
    shuffle(testing_data)
    np.save('train_data.npy', testing_data)
    return testing_data

def load_train_data_NPY():
    data = np.load('train_data.npy')
    return data

def load_test_data_NPY():
    data = np.load('test_data.npy')
    return data
