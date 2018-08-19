from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
import somlib as sl
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import parlib as pl
import natsort
import os
from django.conf import settings

# Create your views here.


def home(request):
    return render(request,'home.html')

def process(request):
    
    if "GET" == request.method:
        return HtppResponce("error")

    myfile  = request.FILES["pcap_file"]
    print(myfile)
    
    #classpercent = SOM(myfile)
    
    return HttpResponse('')

def normalized(csv):
#NORMALIZE PART#
	#print(csv)
	scaler = MinMaxScaler()
	scaler.fit(csv)
	scaler.data_max_
	np.set_printoptions(precision=3)
	np.set_printoptions(suppress=True)
	a = scaler.transform(csv) #normalized array
	return a

def SOM(som):
    
    
    testcap = som
    testfile = os.path.join(settings.BASE_DIR,"static/npy/trys.npy")
    testweights = os.path.join(settings.BASE_DIR,"static/npy/weights.npy")
    testlegends = os.path.join(settings.BASE_DIR,"static/npy/yes.npy")

    pl.csv5(os.path.join(settings.BASE_DIR,"static/chap/a"),testcap)
    tmparr=[]

    for filename in os.listdir(os.path.join(settings.BASE_DIR,"static/chap")):
        if filename.endswith(".csv"): 
            tmparr.append(filename)
            continue
        else:
            continue
    tmparr.sort()
    visual_list = natsort.natsorted(tmparr)
    w = sl.load(testweights)
    newarr = sl.load(testfile)
    sl.dispcolor(newarr)
    newss = sl.load(testlegends)
    legend_red = newss[0]  
    legend_blue = newss[1]
    legend_violet = newss[2]
    legend_yellow = newss[3]
    legend_pink = newss[4]
    legend_grey = newss[5]
    
    print (newss)
    for x in visual_list:
        temp = (os.path.join(settings.BASE_DIR,"static/chap")+x)
        tests = sl.opencsv(temp)
        tests = normalized(tests)
        print(tests)
        hits = sl.som_hits(w, tests)
        name = (os.path.join(settings.BASE_DIR,"static/img") + x +".png")
        print(name)
        sl.disp(newarr,name,hits)
    print("success!")
    return newss