import io
import os

from google.cloud import vision
from google.cloud.vision import types

# 인증하는 방법
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'resources/cloudapi-2eba7a867f32.json'

client = vision.ImageAnnotatorClient()

file_name = os.path.join(os.path.dirname(__file__),'resources/landmark.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.landmark_detection(image=image)
landmarks = response.landmark_annotations

print('Landmarks:')
for landmark in landmarks:
    print(landmarks.description)
    for location in landmark.locations:
        lat_lng = location.lat_lng
        print('Latitude'.format(lat_lng.latitude))
        print('Longitude'.format(lat_lng.longitude))


