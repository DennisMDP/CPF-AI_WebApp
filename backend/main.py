from ImageClassifier import ImageClassifier
from fastapi import FastAPI


app = FastAPI()

classifier = ImageClassifier()

# Endpoint function for getting the predicted class
@app.get("/prediction-stats/class")
async def get_class():
    class_name = classifier.predict_class(probability=False)
    return {"class_name": class_name}

# Endpoint function for getting the predicted class and its probability
@app.get("/prediction-stats/class-and-probability")
async def get_classProb():
    class_name, probability = classifier.predict_class(probability=True)
    return {
        "class_name": class_name,
        "probability": str(probability)
        }