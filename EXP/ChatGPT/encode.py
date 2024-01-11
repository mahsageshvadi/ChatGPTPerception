import base64
from io import BytesIO

import sys
sys.path.append('../EXP/')
import ClevelandMcGill as C
import matplotlib.pyplot as plt

class Encode:
    @staticmethod
    def encode_image(data):
        image = C.Figure12.data_to_image(data)
        plt.axis('off')
        plt.imshow(image)

        image_buffer = BytesIO()
        plt.savefig(image_buffer, format='png', dpi=200)
        image_buffer.seek(0)
        base64_string = base64.b64encode(image_buffer.read()).decode('utf-8')
        image_buffer.close()

        return base64_string