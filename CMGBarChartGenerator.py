import os, sys, time
import pickle
import EXP.ClevelandMcGill as C
import mahotas as mh

from Config import Config, MakeDir, ClearDir

config = Config()

def GenerateCMGBarChart(image_num):


    MakeDir(config.base_dir+"barchart_CMG")
    ClearDir(config.base_dir+"barchart_CMG")
    file_gt = open(config.base_dir + "barchart_CMG/ground_truth.txt", 'w')

    for i in range(image_num):


        data, labels, parameters = C.Figure12.generate_datapoint()
        s_w = C.Figure12.data_to_image(data)
        s_wo = C.Figure12.data_to_image(data, framed=False)

        mh.imsave(config.base_dir + config.chartName.format("Barchart_CMG_fig12_w", i), s_w * 255)
        mh.imsave(config.base_dir + config.chartName.format("Barchart_CMG_fig12_wo", i), s_wo * 255)

        for t in range(len(labels)):
            file_gt.write("%.6f\t" % (labels[t]))

        file_gt.write("\n")


if __name__ == '__main__':
    GenerateCMGBarChart(10)
