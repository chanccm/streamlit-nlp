import streamlit as st
from streamlit import components
import pandas as pd
import re
from gensim import corpora, models


#### variables ####
source_data_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/data/drug_names_kaggle_TASK.xlsx'
lda_saved_model_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/models/lda4.model'
corpora_saved_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/models/lda4_corpus'
topic_count = 4

#### functions ####
def get_medication_name(text):
    
    first_sentence = text.partition('.')[0]
    name = ' '.join(re.findall(r'\b[A-Z][a-z]+|\b[A-Z]\b', first_sentence))
    
    return name

def modify_df(df, list_topic_est):

    # add column for medication name
    df['medication_name'] = df['Introduction'].apply(lambda x: get_medication_name(x))

    # add in topic estimation column
    df['topic_estimation'] = list_topic_est

    # separate topic estimation into columns
    for i in range(topic_count):
        column_name = 'topic' + str(i)
        df[column_name] = 0.0
    for i in range(len(df)):
        for j in df.iloc[i].loc['topic_estimation']:
            for k in range(topic_count):
                if k == j[0]:
                    estimation = j[1]
                    column_name = 'topic' + str(k)
                    df.at[i, column_name] = estimation

    return df



#### app ####
def app():

    st.title('Look up relevant drugs')
    st.write('Topic Model (LDA model) trained on drug descriptions')

    with open('./models/vis4.html', 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1300, height=800, scrolling=False)

    # pulldown menu of drugs
    # user choose name of drug
    # display description
    # display topic probability

    # load model
    lda_fromload = models.LdaModel.load(lda_saved_model_path)
    lda_corpus = corpora.MmCorpus(corpora_saved_path)

    # load dataframe and modify
    df = pd.read_excel(source_data_path,
                        header = 1,
                        usecols = [1])
    
    list_topic_estimation = []
    for i in range(len(lda_corpus)):   
        topic_estimation = lda_fromload.get_document_topics(lda_corpus[i])
        list_topic_estimation.append(topic_estimation)

    df = modify_df(df, list_topic_estimation)

    text = str(df.iloc[1].values)
    st.write(text)

    
    






if __name__ == '__main__':
    app()