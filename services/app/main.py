#import torch
#from diffusers import StableDiffusionPipeline
import uvicorn
from fastapi import FastAPI, Response
from pydantic import BaseModel
from io import BytesIO
from mlconfig import Model


app = FastAPI()
modelobj = Model()
pipeline = modelobj.load()

class Payload(BaseModel):
    text: str

@app.post("/test")
async def test(payload: Payload):
    print(f'Request: {payload}')
    image = pipeline(payload.text).images[0]
    resized_image = image.resize((200, 200))
    buffer = BytesIO()
    resized_image.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()
    return Response(content=image_bytes, media_type="image/jpeg")

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8501)
