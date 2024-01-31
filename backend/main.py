from ImageClassifier import ImageClassifier
from fastapi import FastAPI


app = FastAPI()

classifier = ImageClassifier()

@app.get("/prediction-stats/class")
async def get_class():
    class_name = classifier.predict_class()
    return {"class_name": class_name}