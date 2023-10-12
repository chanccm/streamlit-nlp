"""
This file is the framework for generating multipage Streamlit app.
"""

import streamlit as st

class MultiPage:
    """Framework for combining multiple streamlit apps."""

    def __init__(self) -> None:
        # Constructor calss to generate a list to store all applications as an instance variable
        self.pages = []

    def add_page(self, title, func) -> None:
        # class method to add pages

        """
        Args: 
            title(str): The title of page we are adding to the list of apps
            func: Python function to render this page in Streamlit
        """

        self.pages.append({
                "title": title,
                "function": func
        })

    def run(self):

        #### init ####
        st.set_page_config(
            page_title='NLP for optimization',
            page_icon=' ',
            layout='wide'
        )

        with st.sidebar:

            st.write(
                '''
                # Natural Language Processing
                - sample usages
                '''
            )

            page = st.selectbox('App Menu',
                                self.pages,
                                format_func=lambda page: page['title']
            )

        # run the app function
        page['function']()
       
