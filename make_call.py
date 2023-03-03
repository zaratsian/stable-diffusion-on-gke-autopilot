import requests
from PIL import Image
import io
import argparse

host = '35.224.46.19'
port = '80' # '8501'

r = requests.post(f'http://{host}:{port}/test',json={'text':'surfing goat'})

print('post request complete')

image_bytes = io.BytesIO(r.content)
image = Image.open(image_bytes)
image.save('result.png')
