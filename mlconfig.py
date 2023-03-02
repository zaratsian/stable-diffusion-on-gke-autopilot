
import torch
from diffusers import StableDiffusionPipeline
#from transformers import pipeline

class Model:
    def __init__(self):
        self.model_id="CompVis/stable-diffusion-v1-4"
        self.device="cuda"
        self.cache_dir="/app/"
    
    def load(self):
        pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16, cache_dir=self.cache_dir)
        pipe = pipe.to(self.device)
        return pipe
