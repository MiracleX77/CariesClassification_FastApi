from typing import Optional
from fastapi import File, UploadFile
from fastapi import FastAPI
import uvicorn
import prediction as pred
import json

app =FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/predict")
async def predict_img(file: UploadFile = File(...)):
    image = pred.read_image(file)
    image = pred.preprocess(image)
    predictions = pred.predict(image)
    predictions_jsonable = [(item[0], item[1], float(item[2])) for item in predictions]
    json_predictions = json.dumps(predictions_jsonable)


    return json_predictions
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)