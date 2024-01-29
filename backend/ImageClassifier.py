from PIL import Image
import io
import requests
import tensorflow as tf
import numpy as np


class ImageClassifier:
    
    def __init__(self):
        self.url = "http://192.168.0.50/image.bmp"
        self.image = None
    

    def get_image(self) -> None:
        '''
        Request current image data from web service.
        '''
        response = requests.get(self.url)
        img = response.content
        # store in variable for comparison and classification
        self.image = img
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
    
    def predict_class(self):
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
        # Test the model on random input data.
        input_shape = input_details[0]['shape']
        input_data = img_array
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        output_data = interpreter.get_tensor(output_details[0]['index'])
        print(output_data)
        score = tf.nn.softmax(output_data)

        class_name = class_names[np.argmax(score)]
        
        return class_name
    
    