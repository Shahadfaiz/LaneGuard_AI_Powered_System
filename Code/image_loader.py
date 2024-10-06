# image_loader.py
import streamlit as st
import base64
import os

def render_image():
    """
    Renders the logo_white_new.png image using base64 encoding.
    """
    # Define possible file paths
    possible_paths = [
        "logo_white_new.png",
        "https://github.com/Shahadfaiz/LaneGuard_AI_Powered_System/blob/main/Code/logo_white_new.png",
        os.path.join(os.path.dirname(__file__), "logo_white_new.png"),
    ]

    # Try to find the image file
    for filepath in possible_paths:
        if os.path.exists(filepath):
            mime_type = "png"  # We know it's a PNG file
            with open(filepath, "rb") as f:
                content_bytes = f.read()
            content_b64encoded = base64.b64encode(content_bytes).decode()
            image_string = f'data:image/{mime_type};base64,{content_b64encoded}'
            st.image(image_string, width=300)
            st.success(f"Image loaded successfully from: {filepath}")
            return

    # If image is not found, display an error message
    st.error("Image 'logo_white_new.png' not found in any of the expected locations.")
    
    # Print current working directory and list its contents for debugging
    st.write(f"Current working directory: {os.getcwd()}")
    st.write("Contents of current directory:")
    st.write(os.listdir())
