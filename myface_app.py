#-*- coding:euc-kr -*-
#Python Imaging Library - PIL - PIllow, OpenCV, PIL...
#https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/face_detection/faces.py

import argparse
import os
from google.cloud import vision
from google.cloud.vision import types

from PIL import Image, ImageDraw


# �����ϴ� ���
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'resources/cloudapi-2eba7a867f32.json'

def detect_face(face_file, max_results=4):

    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations

def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

    im.save(output_filename)


#main - �Ķ���ͷ� �׸��Է�, �������, ����� ����
def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:

        faces = detect_face(image, max_results)

        print('Found {} face{}'.format(len(faces), '' if len(faces) == 1 else 's'))
        print('Writing to file {}'.format(output_filename))

        # Reset the file pointer, so we can read the file again

        image.seek(0)
        highlight_faces(image, faces, output_filename)

if __name__ == '__main__':
    #
    # parse = argparse.ArgumentParser(description='���ν����α׷�')
    # parse.add_argument('input_image', help='�м��� ���� �Է�')
    # parse.add_argument('---out', dest='output', default='out.jpg', help='�м� ��� ����� �Է�')
    # parse.add_argument('--max-results', dest='Max_results', default=4, help='��� ����� ')
    # args = parse.parse_args()

    parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')
    parser.add_argument(
        'input_image', help='the image you\'d like to detect faces in.')
    parser.add_argument(
        '--out', dest='output', default='out.jpg',
        help='the name of the output file.')
    parser.add_argument(
        '--max-results', dest='max_results', default=4,
        help='the max results of face detection.')

    args = parser.parse_args()

    main(args.input_image, args.output, args.max_results)
    #main(args.input_image, 'out.png', 4)



