import requests
from PIL import Image
import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, required=False, default="localhost", help='ML Endpoint Host')
parser.add_argument('--port', type=int, required=False, default=80, help='ML Endpoint Port')
parser.add_argument('--text', type=str, required=True,  default="", help='Text to Convert to Image')
args = parser.parse_args()

r = requests.post(f'http://{args.host}:{args.port}/test',json={'text':args.text})

image_bytes = io.BytesIO(r.content)
image = Image.open(image_bytes)
image.save('result.png')
