import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import time

from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet 
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import gensim
from gensim import corpora
from gensim import matutils, models
from gensim.models import CoherenceModel

import pyLDAvis
import pyLDAvis.gensim_models


#### functions ####




#### app ####
def app():

    st.title('Estimate topic for drug of your choice')

    # pulldown menu of drugs
    # user choose name of drug
    # display description
    # display topic probability
    


if __name__ == '__main__':
    app()