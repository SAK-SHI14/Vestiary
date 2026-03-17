import cv2
from cv2 import dnn_superres
import os
import numpy as np

# Singleton model loader
class Upscaler:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Upscaler, cls).__new__(cls)
            cls._instance.sr = dnn_superres.DnnSuperResImpl_create()
            # Check if model exists, if not, we handle it gracefully 
            # (In a real scenario, we'd download it)
            model_path = "EDSR_x4.pb" 
            if os.path.exists(model_path):
                cls._instance.sr.readModel(model_path)
                cls._instance.sr.setModel("edsr", 4)
            else:
                cls._instance.sr = None
        return cls._instance

    def upscale(self, image_path):
        if not os.path.exists(image_path):
            return None
        
        img = cv2.imread(image_path)
        if self.sr:
            return self.sr.upsample(img)
        else:
            # Fallback: bicubic upscaling + sharpening
            h, w, _ = img.shape
            # 1. Upscale
            upscaled = cv2.resize(img, (w*4, h*4), interpolation=cv2.INTER_CUBIC)
            
            # 2. Sharpening (Unsharp Mask)
            gaussian = cv2.GaussianBlur(upscaled, (0, 0), 2.0)
            sharp = cv2.addWeighted(upscaled, 1.5, gaussian, -0.5, 0)
            
            return sharp

def get_upscaled_image(image_path):
    if not os.path.exists(image_path):
        return None
    # Temporarily disable upscaling to avoid artifacts on thumbnails
    img = cv2.imread(image_path)
    if img is None:
        return None
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
