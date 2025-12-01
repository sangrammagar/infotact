from fastapi import FastAPI, File, UploadFile
import numpy as np
import io
from PIL import Image

app = FastAPI(title='Pest Forecaster API')

@app.post('/upload_drone')
async def upload_drone(img: UploadFile = File(...)):
    # Save uploaded file to disk for pipeline (demo)
    content = await img.read()
    img_pil = Image.open(io.BytesIO(content))
    w,h = img_pil.size
    return {'filename': img.filename, 'width': w, 'height': h}

@app.get('/forecast_demo')
def forecast_demo():
    # Return synthetic forecast heatmap summary
    heat = np.random.rand(100,100).tolist()
    return {'heatmap_preview': heat[:2][:2]}
