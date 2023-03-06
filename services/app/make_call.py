# Copyright 2023 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
