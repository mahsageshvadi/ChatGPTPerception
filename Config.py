import numpy as np
import os
import shutil

class Config:
    # The folder of datasets.
    base_dir = os.path.abspath('./dataset')+"/"

    # image configuration
    image_width = 100
    image_height = 100

    chartName = "img_{}_{}.png"

def ClearDir(path):
    if os.path.exists(path):
        print("Resetting the folder.....",path)
        shutil.rmtree(path=path)
    os.mkdir(path)


# Drawing the processing bar
def GetProcessBar(bid, batch_num,dot_num = 40):
    ratio = (bid+1)/batch_num
    delta = 40-(int(ratio*dot_num) + int((1-ratio)*dot_num))
    return '['+'='*int(ratio*dot_num) + '>'+"."*int((1-ratio)*dot_num+delta)+']'


def NormalizeNp(arr):
    max = np.sum(arr)
    return np.array(arr/max)


def GetAllFiles(dirpath):
    filepaths = []
    for root, dirs, files in os.walk(dirpath):

        for f in files:
            filepaths.append(os.path.join(root, f))
    return filepaths

def GetFileCountIn(dirpath):
    for root, dirs, files in os.walk(dirpath):
        return len(files)



def ReadLinesInFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines

def ClearDir(path):
    if os.path.exists(path):
        print("Resetting the folder.....",path)
        shutil.rmtree(path=path)
    os.mkdir(path)

def MakeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def RemoveDir(path):
    if os.path.exists(path):
        os.remove(path)
