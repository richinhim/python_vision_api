import io
import os

from google.cloud import vision
from google.cloud.vision import types

# 인증하는 방법
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'resources/cloudapi-2eba7a867f32.json'

client = vision.ImageAnnotatorClient()

file_name = os.path.join(os.path.dirname(__file__),'resources/text.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs logo detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations

print('Texts:')
for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))



