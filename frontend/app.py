import streamlit as st
import requests
from PIL import Image
import io
# from time import sleep
# import tensorflow as tf
# import numpy as np

IMAGE_URL = "http://192.168.0.50/image.bmp"

URL = "http://127.0.0.1:8000"
ENDPOINT_CLASS = URL + "/prediction-stats/class"

# create image classifier object
# image_classifier = ImageClassifier()

# Set Streamlit title
st.title("Image Classifier")

# Set default image
default_img = Image.open("default_img.png")

# Display default image
image_label = st.image(default_img, caption="Default Image", use_column_width=True)

# Text label for predicted class
class_label = st.empty()

def test():
    response = requests.get(ENDPOINT_CLASS).json()
    class_name = response["class_name"]
    image_label.image(Image.open("test_img.png"))
    
    class_label.text(f"Klasse: {class_name}") 

st.button(label="Testbild", on_click=test())

# #------------
# sleep(5)
# image_label.image(Image.open("default.png"))
# class_label.text("default")
# sleep(5)
# image_label.image(Image.open("default_img.png"))
# class_label.text("default_image")
# sleep(5)
# img = Image.open("test_img.png").convert("RGB")
# # Resize
# img = img.resize((224, 224))
# # Change to array object that contains the rgb values for each pixel
# img_array = tf.keras.utils.img_to_array(img)
# img_array = tf.expand_dims(img_array, 0)
# # Class names 
# class_names = ['gummibaer', 'handyschale', 'handyschale_falsch', 'handyschale_umgedreht', 'leer', 'schokolade']
# TF_MODEL_FILE_PATH = 'cpf_new_full.tflite'
# # Load the TFLite model and allocate tensors.
# interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
# interpreter.allocate_tensors()
# # Get input and output tensors.
# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()
# # Test the model on random input data.
# input_shape = input_details[0]['shape']
# input_data = img_array
# interpreter.set_tensor(input_details[0]['index'], input_data)
# interpreter.invoke()

# # The function `get_tensor()` returns a copy of the tensor data.
# # Use `tensor()` in order to get a pointer to the tensor.
# output_data = interpreter.get_tensor(output_details[0]['index'])
# print(output_data)
# score = tf.nn.softmax(output_data)

# class_name = class_names[np.argmax(score)]


# image_label.image(Image.open("test_img.png"))
# class_label.text(f"Klasse: {class_name}")
# sleep(10)
# image_label.image(Image.open("default_img.png"))
# class_label.text("default_image")
# sleep(10)
# image_label.image(Image.open("default.png"))
# class_label.text("default")
# #------------

# def get_image(self) -> None:
#     '''
#     Request current image data from web service.
#     '''
#     response = requests.get(self.url)
#     img = response.content
#     # store in variable for comparison and classification
#     self.image = img
#     return


# def update_gui():
#     '''
#     Check web service if there is a new picture.
#     If there is a new picture: Predict the class and update GUI with new picture and associated class.
#     '''
    
#     # call current image from web service
#     img = image_classifier.get_image()
    
#     # check if the image has been changed
#     if not image_classifier.are_images_equal():
#         # convert image for GUI label
#         # img_pil = Image.open(io.BytesIO(img)).convert("RGB")
#         # Display the updated image
#         image_label.image(img, use_column_width=True)
#         # predict image class
#         image_class = image_classifier.predict_class()
#         # update class label
#         class_label.text(f"Klasse: {image_class}")
#         # warning bell if the class is "handyschale_falsch"
#         if image_class == "handyschale_falsch":
#             st.balloons()  # Streamlit balloons effect as a substitute for the root.bell()
    
#     # repeat update-function every 2 seconds
#     sleep(2)
#     update_gui()

# # Start update-loop
# # update_gui()