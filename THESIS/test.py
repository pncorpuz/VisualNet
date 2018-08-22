import somlib as sl
import parlib as pl
import numpy as np
import os
import natsort


pcapname = "1gaming.pcap"
directory = "csv/"
filename = "csv"
somsize = 20
ksize = 6

pl.csv5(directory+filename,pcapname)
tmparr=[]
for filename in os.listdir(directory):
	if filename.endswith(".csv"):
		tmparr.append(filename)
	else:
		continue
visual_list = natsort.natsorted(tmparr)

label = np.load("label.npy")
kmap = np.load("kmap.npy")
weights = np.load("weights.npy")

count = 0
for x in visual_list:
	count = count + 1
	temp = directory+x
	csv = sl.opencsv(temp)
	norm = sl.normalized(csv)
	hits = sl.som_hits(weights, norm)
	name = ("img/" + x + ".png")
	sl.hit_overlap(kmap,hits,count)
	sl.disp(kmap,name,hits,label)
