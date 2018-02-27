import os
from os.path import basename
path="/home/ml/Desktop/Data_voc_format/New"  
dirList=os.listdir(path)
with open("output1.txt", "w") as f:
    for filename in dirList:
        print basename(os.path.splitext(filename)[0])
        f.write("%s\n" %(basename(os.path.splitext(filename)[0]))) 
