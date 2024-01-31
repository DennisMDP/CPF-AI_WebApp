import streamlit as st
import requests
from PIL import Image
from time import sleep


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

def get_class():
    response = requests.get(ENDPOINT_CLASS).json()
    class_name = response["class_name"]
    return class_name

def get_image():
    '''
    Request current image data from web service.
    '''
    response = requests.get(IMAGE_URL)
    img = response.content
    return img

def update_gui():
    '''
    Check web service if there is a new picture.
    If there is a new picture: Predict the class and update GUI with new picture and associated class.
    '''
    img = get_image()
    image_label.image(img, use_column_width=True)
    image_class = get_class()
    # update class label
    class_label.text(f"Klasse: {image_class}")
    # warning bell if the class is "handyschale_falsch"
    if image_class == "handyschale_falsch":
        st.balloons()  # Streamlit balloons effect as a substitute for the root.bell()

    

def main():
    while True:
        update_gui()
        sleep(1)


if __name__ == "__main__":
    main()