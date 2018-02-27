import os
import shutil

itemPath = []
dirPath = []
#Directory where your crawler saves the images
rootDir = "/home/ml/Desktop/license_plate/21_2_18/VOC_2007"
#Directory where you want to organize your images
destDir = "/home/ml/Desktop/license_plate/21_2_18/VOC2007"

#find all the jpg files and save the path
def openFolder(rootDir):
    path = []
    global itemPath
    global dirPath
    for listItem in os.listdir(rootDir):
        path = os.path.join(rootDir,listItem)
        if os.path.isdir(path):
            dirPath.append(path)
            openFolder(path)
        if os.path.isfile(path) and path[-3:]=="jpg":
            itemPath.append(path)


if __name__ == "__main__":
    openFolder(rootDir)
    files=itemPath
    #Give each image a unique and consistent name
    counter = 0
    progress = 0
    length = len(files)
    #print every 5%
    delta = int(length/20)
    for item in files:
        if counter%delta == 0:
            #print("Current Progress: "+progress+"%")
            progress += 5
        shutil.move(item,destDir+"/"+str(counter).zfill(6)+".jpg")
        counter += 1
