from ImageClassifier import ImageClassifier
from fastapi import FastAPI


URL = "http://192.168.0.50/image.bmp"

app = FastAPI()


@app.get("/prediction-stats/class")
async def get_class():
    classifier = ImageClassifier()
    class_name = classifier.predict_class()
    return {"class_name": class_name}