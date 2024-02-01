import streamlit as st
import requests
from PIL import Image
from time import sleep
import numpy as np


IMAGE_URL = "http://192.168.0.50/image.bmp"

URL = "http://127.0.0.1:8000"
ENDPOINT_CLASS = URL + "/prediction-stats/class"


# Set Streamlit title
st.title("Image Classifier")

# Set default image
default_img = Image.open("default_img.png")

# Display default image
image_label = st.image(default_img, caption="Default Image", use_column_width=True)

# Text label for predicted class
class_label = st.empty()


current_img = default_img

    
def get_image():
    '''
    Request current image data from web service.
    '''
    response = requests.get(IMAGE_URL)
    img = response.content
    return img

def are_images_equal(current_img, new_img):
    '''
    Get bool value that states if the new image is equal to the current image.
    '''
    return np.array_equal(np.array(current_img), np.array(new_img))

def get_class():
    response = requests.get(ENDPOINT_CLASS).json()
    class_name = response["class_name"]
    return class_name

def update_gui(img, img_class):
    '''
    Check web service if there is a new picture.
    If there is a new picture: Predict the class and update GUI with new picture and associated class.
    '''
    image_label.image(img, use_column_width=True)
    
    # update class label
    class_label.text(f"Klasse: {img_class}")
    # warning bell if the class is "handyschale_falsch"
    if img_class == "handyschale_falsch":
        st.balloons()  # Streamlit balloons effect as a substitute for the root.bell()

    

def main():
    while True:
        img = get_image()
        if are_images_equal(current_img=current_img, new_img=img):
            img_class = get_class()
            update_gui(img=img, img_class=img_class)
        sleep(0.3)


if __name__ == "__main__":
    main()