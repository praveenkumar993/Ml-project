from django.db import models
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

#import cv2
import numpy as np
import pickle
#import pyreadstat
import json

import pandas as pd 



# Testing phase

knn = pickle.load(open(r"C:\Users\dsp96\Desktop\SMART_FARM\FRONT END\knn_smart.pkl", 'rb'))
dt = pickle.load(open(r"C:\Users\dsp96\Desktop\SMART_FARM\FRONT END\dt_smart.pkl", 'rb'))


df = pd.read_csv(r'C:\Users\dsp96\Desktop\SMART_FARM\FRONT END\test.csv')

def predict(algo,row):
	#print(x.columns)
	test_data=df.iloc[row].values.reshape(1,-1)
	print(test_data.shape)
	#print(test_data.columns)
	if algo == 'knn':
		y_pred = knn.predict(test_data)
	else:
		y_pred = dt.predict(test_data)
	return y_pred
