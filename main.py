
#import torch
#from diffusers import StableDiffusionPipeline
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from mlconfig import Model

app = FastAPI()
modelobj = Model()
pipeline = modelobj.load()

class Payload(BaseModel):
    text: str

@app.post("/test")
async def test(payload: Payload):
    print(f'Payload: {payload}')
    image = pipeline(payload.text).images[0]
    return payload

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8501)
