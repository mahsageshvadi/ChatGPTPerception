import base64
import cv2
import numpy as np

import sys
sys.path.append('../EXP/')
import ClevelandMcGill as C

class Encode:
    @staticmethod
    def encode__figure12_image():
        data, labels, parameters = C.Figure12.generate_datapoint()
        image = C.Figure12.data_to_image(data)

        return image
    
    @staticmethod
    def encode__figure3_image():
        data, labels = C.Figure3.generate_datapoint()
        image = C.Figure3.data_to_barchart(data)

        return image
    
    @staticmethod
    def encode__figure4_image():
        data, labels = C.Figure4.generate_datapoint()
        image = C.Figure4.data_to_type1(data)

        return image
    
    @staticmethod
    def encode__figure1_angle_image():
        sparse, image, label, parameters = C.Figure1.angle()

        return image
    
    @staticmethod
    def encode__figure1_position_common_scale_image():
        sparse, image, label, parameters = C.Figure1.position_common_scale()

        return image
    
    @staticmethod
    def encode__figure1_length_image():
        sparse, image, label, parameters = C.Figure1.length([False, False, False])

        return image
    
    @staticmethod
    def encode__figure1_direction_image():
        sparse, image, label, parameters = C.Figure1.direction()

        return image

    @staticmethod
    def encode__figure1_area_image():
        sparse, image, label, parameters = C.Figure1.area()

        return image
    
    @staticmethod
    def encode__figure1_volume_image():
        sparse, image, label, parameters = C.Figure1.volume()

        return image
    

    @staticmethod
    def encode__figure1_curvature_image():
        sparse, image, label, parameters = C.Figure1.curvature()

        return image
    
    @staticmethod
    def encode__figure1_shading_image():
        sparse, image, label, parameters = C.Figure1.shading()

        return image
    
    
    @staticmethod
    def encode__weber_base10():
        image, label = C.Weber.base10()

        return image
    
    