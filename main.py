from fileinput import filename
from fastapi  import FastAPI, File, UploadFile
import os
import typing as List
import shutil

from model import predict
from train import train

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello'

# train and save model
@app.post("/train")
async def train():
    train()
    return 'train & save success'
    
# store model
@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# prediction
@app.post("/predict")
async def get_prediction():
    pred = predict()
    return pred

# uploadfile 
# http --form http://localhost:8000/uploadfile file@./filename

# prediction
# http --POST http://localhost:8000/predict
