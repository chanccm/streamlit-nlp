import streamlit as st
from streamlit import components

#### functions ####


#### app ####
def app():

    st.title('Visualize a pretrained Topic Model (LDA model)')

    with open('./models/vis4.html', 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1300, height=800, scrolling=False)


if __name__ == '__main__':
    app()