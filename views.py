from django.shortcuts import render

from .models import predict
from django.shortcuts import render
import requests
import numpy as np
import pandas as pd

def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)
    #print(lines_list)
    return lines_list



# Create your views here.
def home(request):
	return render(request,'index.html')

def input(request):
    file_name = 'account.txt'
    name = request.POST.get('name')
    password = request.POST.get('password')
    account_list = read_file(file_name)
    print(name)
    print(password)
    for i in account_list:

        if i[0] == name  and i[1] == password:
            print(i[0])
            print(i[1])
            return render(request,'input.html')
        else:
            return HttpResponse('Wrong Password or Name', content_type='text/plain')

class_names = ['Clay-Drip Irrigation', 'Saline-Drip Irrigation',
       'Clay-Sprinkler Irrigation', 'Black lava soil-Tube Well',
       'Chalky (Calcareous)-Sprinkler Irrigation',
       'Sandy-Drip Irrigation', 'Chalky (Calcareous)-Canal Irrigation',
       'Nitrogenous-Drip Irrigation', 'Saline-Tube Well',
       'Nitrogenous-Tube Well', 'Nitrogenous-Canal Irrigation',
       'Nitrogenous-Sprinkler Irrigation', 'Alkaline-Drip Irrigation',
       'Black lava soil-Sprinkler Irrigation',
       'Sandy-Sprinkler Irrigation', 'Loamy-Tube Well',
       'Black lava soil-Canal Irrigation', 'Clay-Tube Well',
       'Chalky (Calcareous)-Tube Well', 'Saline-Canal Irrigation',
       'Loamy-Drip Irrigation', 'Sandy-Tube Well',
       'Loamy-Canal Irrigation', 'Alkaline-Canal Irrigation',
       'Alkaline-Tube Well', 'Black lava soil-Drip Irrigation',
       'Alkaline-Sprinkler Irrigation', 'Sandy-Canal Irrigation',
       'Loamy-Sprinkler Irrigation', 'Saline-Sprinkler Irrigation',
       'Clay-Canal Irrigation', 'Chalky (Calcareous)-Drip Irrigation']


def output(request):
	algo=request.POST.get('algo')
	row=int(request.POST.get('row'))
	out=predict(algo,row)
	print(out)
	classes = class_names[int(out)]

	print(classes)
	return render(request,'output.html',{'out':classes})
