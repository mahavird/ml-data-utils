import os
from os.path import basename
#path="/home/ml/Desktop/license_plate/VOC2007/Annotations"  
#dirList=os.listdir(path)
with open("test.txt", "w") as f:
    for i in range(21100,21392):
    	print i
    	if (i<10):
    		f.write("00000%s\n" %(i))
    	elif (i<100):
    		f.write("0000%s\n" %(i))
    	elif (i<1000):
    		f.write("000%s\n" %(i))
    	else:
    		f.write("0%s\n" %(i))


