import os
import io

from google.cloud import speech
from google.cloud import speech
from google.cloud.speech import types
from google.cloud.speech import enums

# 인증
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'resources/cloudapi-2eba7a867f32.json'


client = speech.SpeechClient()

file_name = os.path.join(os.path.dirname(__file__),'./audio.raw')

# Loads the image into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
