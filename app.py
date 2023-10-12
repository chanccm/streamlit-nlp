import streamlit as st

from multipage import MultiPage
from pages import visualize_model, get_text_topic_estimation

# Create an instance of app
app = MultiPage()

# Add app pages
app.add_page('Visualize pretrained model', visualize_model.app)
app.add_page('Train your own model', get_text_topic_estimation.app)

# Main app
app.run()
