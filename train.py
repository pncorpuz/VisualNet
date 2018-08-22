import somlib as sl
import numpy as np


csvname = "input.csv"
somsize = 20
ksize = 6

csv = sl.opencsv(csvname)
norm = sl.normalize(csv)
weights = sl.som(norm,somsize)
label = sl.cluster_coloring(weights,norm,csv)

kmean = sl.kmeans(ksize,weights)
kmap = np.reshape(kmean,(somsize,somsize))

temp = sl.determine_cluster(label,kmap,ksize)
perc = sl.toperc(temp)

sl.pie(perc)


np.save("kmap",kmap)
np.save("weights",weights)
