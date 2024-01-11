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

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure3_image():
        data, labels = C.Figure3.generate_datapoint()
        image = C.Figure3.data_to_barchart(data)
        
        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure4_image():
        data, labels = C.Figure4.generate_datapoint()
        image = C.Figure4.data_to_type1(data)

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_angle_image():
        sparse, image, label, parameters = C.Figure1.angle()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_position_common_scale_image():
        sparse, image, label, parameters = C.Figure1.position_common_scale()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_length_image():
        sparse, image, label, parameters = C.Figure1.length([False, False, False])

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_direction_image():
        sparse, image, label, parameters = C.Figure1.direction()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_area_image():
        sparse, image, label, parameters = C.Figure1.area()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_volume_image():
        sparse, image, label, parameters = C.Figure1.volume()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    

    @staticmethod
    def encode__figure1_curvature_image():
        sparse, image, label, parameters = C.Figure1.curvature()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale
    
    @staticmethod
    def encode__figure1_shading_image():
        sparse, image, label, parameters = C.Figure1.shading()

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0


        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png, grayscale