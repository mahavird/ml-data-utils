import os,sys
folder = '/home/lprindia/projects/train_brand_lp/VOC2007/rename_test'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.xml.xml', '.xml')
       output = os.rename(infilename, newname)