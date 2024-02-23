import streamlit as st
import requests
from PIL import Image
from time import sleep

# CP Factory camera image endpoint
IMAGE_URL = "http://192.168.0.50/image.bmp"
# Class prediction endpoint
ENDPOINT_CLASS = "http://192.168.0.248:8000/prediction-stats/class"

# Map the endpoint-results to strings for the GUI
class_mapping = {
    "handyschale": "Handyschale",
    "handyschale_umgedreht": "Handyschale gewendet",
    "handyschale_falsch": "Handyschale falsch herum",
    "leer": "Leerer Teileträger",
    "schokolade": "Schokoladenbox",
    "gummibaer": "Gummibärenbox"
}


# Set Streamlit title
st.title("CP Factory ComputerVision")

# Set default image
default_img = Image.open("default_img.png")

# Display default image
image_label = st.image(default_img, use_column_width=True)

# Text label for predicted class
st.markdown("""
	<style>
	.big-font {
	    font-size:30px !important;
	}
	</style>
	""", unsafe_allow_html=True)

class_label = st.markdown('<p class="big-font">Default Image</p>', unsafe_allow_html=True)


def get_class():
    '''
    Request class prediction.
    '''
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
    class_label.markdown(f'<p class="big-font">Erkanntes Bauteil: {class_mapping[image_class]}</p>', unsafe_allow_html=True)
    # warning bell if the class is "handyschale_falsch"
    # if image_class == "handyschale_falsch":
    #     st.warning('Bauteil falsch herum!', icon="⚠️")

    
def main():
    while True:
        # Update every 1 second
        update_gui()
        sleep(1)


if __name__ == "__main__":
    main()
