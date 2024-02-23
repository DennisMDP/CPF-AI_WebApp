from PIL import Image
import io
import requests
import tensorflow as tf
import numpy as np


class ImageClassifier:
    
    def __init__(self):
        # REST endpoint for cp factory camera image
        self.url = "http://192.168.0.50/image.bmp"
        # Variable for storing the current image
        self.image = None
    

    def get_image(self) -> None:
        '''
        Request current image data from web service.
        '''
        response = requests.get(self.url)
        # store in variable for comparison and classification
        self.image = response.content
        return
    
    def process_image(self):
        '''
        Preprocess image data to prepare it for the ML-model.
        '''
        img = Image.open(io.BytesIO(self.image)).convert("RGB")
        # Resize
        img = img.resize((224, 224))
        # Change to array object that contains the rgb values for each pixel
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        return img_array
    
    def predict_class(self, probability: bool) -> str:
        '''
        Preditct the class of the image using the tflite-model.
        '''
        self.get_image()
        # Prepare image to match the input requirements of the model
        img_array = self.process_image()
        # Class names 
        class_names = ['gummibaer', 'handyschale', 'handyschale_falsch', 'handyschale_umgedreht', 'leer', 'schokolade']
        TF_MODEL_FILE_PATH = 'cpf_new_full.tflite'
        # Load the TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
        interpreter.allocate_tensors()
        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        input_data = img_array
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # The function `get_tensor()` returns a copy of the tensor data.
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        # Get a matrix of the prediction score/probapilities
        score = tf.nn.softmax(output_data)
        
        # Get the index of the class with the highest probability
        predicted_class_index = np.argmax(score)
        
        # If probabili is set to True, return class and probability    
        if probability:
            # Get the probability of the predicted class
            predicted_probability = score[0][predicted_class_index].numpy()
            return class_names[predicted_class_index], predicted_probability
        
        # If probabili is set to False, return only class
        else:
            return class_names[predicted_class_index]
    