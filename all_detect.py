"""
Google Cloud Vision API.
Example Usage:
python all_detect.py text ./resources/wakeupcat.jpg
python all_detect.py labels ./resources/landmark.jpg
python all_detect.py web ./resources/landmark.jpg
python all_detect.py web-uri http://wheresgus.com/dog.JPG
python all_detect.py faces-uri gs://your-bucket/file.jpg
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/detect/detect.py

"""

import argparse
import io

import os
from google.cloud import vision
from google.cloud.vision import types

# 인증하는 방법
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'resources/cloudapi-2eba7a867f32.json'

def detect_faces(path):

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'resources/cloudapi-2eba7a867f32.json'

    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.face_detection(image=image)
    faces = response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
#
# def detect_faces_uri(uri):


def detect_labels(path):

    client = vision.ImageAnnotatorClient()

    # [START migration_label_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)
#
# def detect_labels_uri(uri):

def detect_landmarks(path):
    client = vision.ImageAnnotatorClient()

    # [START migration_landmark_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print('Landmarks:')

    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print('Latitude'.format(lat_lng.latitude))
            print('Longitude'.format(lat_lng.longitude))
#
# def detect_landmarks_uri(uri):


def detect_logos(path):
    client = vision.ImageAnnotatorClient()

    # [START migration_logo_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)

# def detect_logos_uri(uri):

def detect_safe_search(path):
    client = vision.ImageAnnotatorClient()

    # [START migration_safe_search_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Safe search:')

    print('adult: {}'.format(likelihood_name[safe.adult]))
    print('medical: {}'.format(likelihood_name[safe.medical]))
    print('spoofed: {}'.format(likelihood_name[safe.spoof]))
    print('violence: {}'.format(likelihood_name[safe.violence]))
#
# def detect_safe_search_uri(uri):

def detect_text(path):
    client = vision.ImageAnnotatorClient()

    # [START migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
#
# def detect_text_uri(uri):

def detect_properties(path):
    client = vision.ImageAnnotatorClient()

    # [START migration_image_properties]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))
#
# def detect_properties_uri(uri):

#
def detect_web(path):
    client = vision.ImageAnnotatorClient()

    # [START migration_web_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.web_detection(image=image)
    notes = response.web_detection

    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')

        for page in notes.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if notes.full_matching_images:
        print('\n{} Full Matches found: '.format(
            len(notes.full_matching_images)))

        for image in notes.full_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.partial_matching_images:
        print('\n{} Partial Matches found: '.format(
            len(notes.partial_matching_images)))

        for image in notes.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.web_entities:
        print('\n{} Web entities found: '.format(len(notes.web_entities)))

        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))

def detect_web_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.web_detection(image=image)
    notes = response.web_detection

    if notes.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved')

        for page in notes.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if notes.full_matching_images:
        print('\n{} Full Matches found: '.format(
            len(notes.full_matching_images)))

        for image in notes.full_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.partial_matching_images:
        print('\n{} Partial Matches found: '.format(
            len(notes.partial_matching_images)))

        for image in notes.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if notes.web_entities:
        print('\n{} Web entities found: '.format(len(notes.web_entities)))

        for entity in notes.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))
# def detect_crop_hints(path):
#
# def detect_crop_hints_uri(uri):
#
#
# def detect_document(path):
#
# def detect_document_uri(uri):

def run_local(args):
    if args.command == 'faces':
        detect_faces(args.path)
    elif args.command == 'labels':
        detect_labels(args.path)
    elif args.command == 'landmarks':
        detect_landmarks(args.path)
    elif args.command == 'text':
        detect_text(args.path)
    elif args.command == 'logos':
        detect_logos(args.path)
    # elif args.command == 'safe-search':
    #     detect_safe_search(args.path)
    # elif args.command == 'properties':
    #     detect_properties(args.path)
    elif args.command == 'web':
        detect_web(args.path)
    # elif args.command == 'crophints':
    #     detect_crop_hints(args.path)
    # elif args.command == 'document':
    #     detect_document(args.path)
#
#
def run_uri(args):
#     if args.command == 'text-uri':
#         detect_text_uri(args.uri)
#     elif args.command == 'faces-uri':
#         detect_faces_uri(args.uri)
#     elif args.command == 'labels-uri':
#         detect_labels_uri(args.uri)
#     elif args.command == 'landmarks-uri':
#         detect_landmarks_uri(args.uri)
#     elif args.command == 'logos-uri':
#         detect_logos_uri(args.uri)
#     elif args.command == 'safe-search-uri':
#         detect_safe_search_uri(args.uri)
#     elif args.command == 'properties-uri':
#         detect_properties_uri(args.uri)
    if args.command == 'web-uri':
        detect_web_uri(args.uri)
#     elif args.command == 'crophints-uri':
#         detect_crop_hints_uri(args.uri)
#     elif args.command == 'document-uri':
#         detect_document_uri(args.uri)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    detect_faces_parser = subparsers.add_parser('faces', help=detect_faces.__doc__)
    detect_faces_parser.add_argument('path')
    #
    # faces_file_parser = subparsers.add_parser('faces-uri', help=detect_faces_uri.__doc__)
    # faces_file_parser.add_argument('uri')

    detect_labels_parser = subparsers.add_parser('labels', help=detect_labels.__doc__)
    detect_labels_parser.add_argument('path')
    #
    # labels_file_parser = subparsers.add_parser('labels-uri', help=detect_labels_uri.__doc__)
    # labels_file_parser.add_argument('uri')

    detect_landmarks_parser = subparsers.add_parser('landmarks', help=detect_landmarks.__doc__)
    detect_landmarks_parser.add_argument('path')

    # landmark_file_parser = subparsers.add_parser('landmarks-uri', help=detect_landmarks_uri.__doc__)
    # landmark_file_parser.add_argument('uri')

    detect_text_parser = subparsers.add_parser('text', help=detect_text.__doc__)
    detect_text_parser.add_argument('path')

    # text_file_parser = subparsers.add_parser('text-uri', help=detect_text_uri.__doc__)
    # text_file_parser.add_argument('uri')

    detect_logos_parser = subparsers.add_parser('logos', help=detect_logos.__doc__)
    detect_logos_parser.add_argument('path')

    # logos_file_parser = subparsers.add_parser('logos-uri', help=detect_logos_uri.__doc__)
    # logos_file_parser.add_argument('uri')
    #
    # safe_search_parser = subparsers.add_parser('safe-search', help=detect_safe_search.__doc__)
    # safe_search_parser.add_argument('path')
    #
    # safe_search_file_parser = subparsers.add_parser('safe-search-uri', help=detect_safe_search_uri.__doc__)
    # safe_search_file_parser.add_argument('uri')
    #
    # properties_parser = subparsers.add_parser('properties', help=detect_properties.__doc__)
    # properties_parser.add_argument('path')
    #
    # properties_file_parser = subparsers.add_parser( 'properties-uri', help=detect_properties_uri.__doc__)
    # properties_file_parser.add_argument('uri')

    # 1.1 Vision features
    # web_parser = subparsers.add_parser('web', help=detect_web.__doc__)
    # web_parser.add_argument('path')

    web_uri_parser = subparsers.add_parser('web-uri', help=detect_web_uri.__doc__)
    web_uri_parser.add_argument('uri')
    #
    # crop_hints_parser = subparsers.add_parser('crophints', help=detect_crop_hints.__doc__)
    # crop_hints_parser.add_argument('path')
    #
    # crop_hints_uri_parser = subparsers.add_parser('crophints-uri', help=detect_crop_hints_uri.__doc__)
    # crop_hints_uri_parser.add_argument('uri')
    #
    # document_parser = subparsers.add_parser('document', help=detect_document.__doc__)
    # document_parser.add_argument('path')
    #
    # document_uri_parser = subparsers.add_parser('document-uri', help=detect_document_uri.__doc__)
    # document_uri_parser.add_argument('uri')

    args = parser.parse_args()

    if ('uri' in args.command):
        run_uri(args)
        # pass
    else:
        run_local(args)