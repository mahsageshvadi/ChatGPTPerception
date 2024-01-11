import base64
from io import BytesIO
import cv2
import numpy as np

import sys
sys.path.append('../EXP/')
import ClevelandMcGill as C
import matplotlib.pyplot as plt

class Encode:
    @staticmethod
    def encode_image():
        data, labels, parameters = C.Figure12.generate_datapoint()
        image = C.Figure12.data_to_image(data)

        # Convert to grayscale
        size = image.shape[0]
        grayscale = np.zeros((size,size), dtype=np.uint8)
        grayscale[image==0] = 255
        grayscale[image==1] = 0
        plt.axis('off')
        plt.imshow(grayscale, cmap='gray')

        rgb = np.stack((grayscale,grayscale,grayscale),axis=-1)
        _, png = cv2.imencode('.png', rgb)

        b64_png = base64.b64encode(png.tobytes()).decode('utf-8')

        return b64_png