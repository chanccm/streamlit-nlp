import streamlit as st

#### functions ####


#### app ####
def app():

    st.title('Visualize a pretrained Topic Model112323 blahblahzz')

    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')


if __name__ == '__main__':
    app()