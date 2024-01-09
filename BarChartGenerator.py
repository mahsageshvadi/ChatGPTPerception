import cv2
import numpy as np
import shutil
import os

from Config import Config, MakeDir

config = Config()


#  set the RANGE of object NUMBER for both training and testing set respectively
min_obj = 3

def Normalize(arr):
    return arr / np.sum(arr)

# generate a chart with number=num objects.
def GenerateOneBarChart(num, backgroundColor = False, size = config.image_width):

    color = tuple(np.random.choice(range(256), size=3))
    thickness = np.random.randint(1, 3)  # line thickness.   (random)

    if color:
        image = np.full((size, size, 3), color, dtype=np.uint8)
    else:
        image = np.ones(shape=(size, size, 1))
    heights = np.random.randint(10,80,size=(num))

    barWidth = int( (size-3*(num+1)-3)//num * (np.random.randint(50,100)/100.0) )
    barWidth = max(barWidth, 4)
    spaceWidth = (size-(barWidth)*num)//(num+1)

    sx = (size - barWidth*num - spaceWidth*(num-1))//2
    for i in range(num):

        sy = size - 1
        ex = sx + barWidth
        ey = sy - heights[i]

        cv2.rectangle(image,(sx,sy),(ex,ey),0,thickness)
        sx = ex + spaceWidth

    # add noise
    noises = np.random.uniform(0, 0.05, (size, size,1))
    image = image + noises
    _min = image.min()
    _max = image.max()
    image -= _min
    image /= (_max - _min)
    heights = heights.astype('float32')
    max_height = max(heights)

    for i in range(len(heights)):
        heights[i] /= max_height

    return image, heights

def ClearDir(path):
    if os.path.exists(path):
        print("Resetting the folder.....",path)
        shutil.rmtree(path=path)
    os.mkdir(path)




def GenerateDataSetBarCharts(image_num, number_of_bars, backgroundColor=False):

    MakeDir(config.base_dir+"barchart")
    ClearDir(config.base_dir+"barchart")

    _images = []
    _labels = []

    file_gt = open(config.base_dir + "barchart/ground_truth.txt" , 'w')

    for i in range(image_num):

        image, featureVector = GenerateOneBarChart(number_of_bars, backgroundColor=backgroundColor)
        featureVector = np.array(featureVector)

        if i % 5000 == 0:
            print("   id {} (obj_num = {})".format(i, featureVector.shape[0]))

        if not backgroundColor:
            image = np.concatenate((image,image,image), axis=-1)
        label = np.zeros(number_of_bars,dtype='float32')
        label[:len(featureVector)] = featureVector

        _images.append(image)
        _labels.append(label)

        cv2.imwrite(config.base_dir + "/barchart/"+ config.chartName.format("Barchart", i), image * 255)
        for t in range(len(featureVector)):
            file_gt.write("%.6f\t" % (featureVector[t]))
        for t in range(number_of_bars - len(featureVector)):
            file_gt.write("0.00\t")
        file_gt.write("\n")


    _images = np.array(_images,dtype='float32')
    _labels = np.array(_labels,dtype='float32')


    return _images,_labels

if __name__ == '__main__':


    GenerateDataSetBarCharts(10, 5, backgroundColor=True);