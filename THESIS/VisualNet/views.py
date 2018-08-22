from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
import somlib as sl
import numpy as np
import parlib as pl
import natsort
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    return render(request,'home.html')

def process(request):
    
    if "GET" == request.method:
        return HtppResponce("error")

    myfile  = request.FILES["pcap_file"]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name,myfile)
    uploaded_file_url = fs.url(filename)
    
    print("YOHOOO")
    print(uploaded_file_url)

    files = os.listdir(os.path.join(settings.BASE_DIR,'static/img'))
    files.sort
    classpercent = SOM(uploaded_file_url)
    fs.delete(filename)
    
    context={
        'files':files
        
    }
    
    return render(request,'process.html',context)

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
    
    pcapname = som
    directory = os.path.join(settings.BASE_DIR,"static/chap/")
    filename = "csv"
    somsize = 20
    ksize = 6
    
    pl.csv5(directory+filename,pcapname)
    temparr = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            temparr.append(filename)
        else:
            continue
    visual_list = natsort.natsorted(temparr)
    kmap = np.load(os.path.join(settings.BASE_DIR,"static/npy/kmap.npy"))
    weights = np.load(os.path.join(settings.BASE_DIR,"static/npy/weights.npy"))
    for x in visual_list:
        temp = directory+x
        csv = sl.opencsv(temp)
        norm = sl.normalized(csv)
        hits = sl.som_hits(weights, norm)
        #name = ("img/" + x + ".png")
        name = (os.path.join(settings.BASE_DIR,"static/img/") + x + ".png")
        sl.disp(kmap,name,hits)
    
    

    