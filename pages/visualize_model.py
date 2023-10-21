# this page displays trained LDA model
# allow user to see list of medications in specific topic


import streamlit as st
from streamlit import components
import pandas as pd
import re
from gensim import corpora, models


#### variables ####
source_data_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/data/drug_names_kaggle_TASK.xlsx'
lda_saved_model_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/models/lda5.model'
corpora_saved_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/models/lda5_corpus'
visualization_path = '/Users/carmen/Documents/machine_learning_exercises/streamlit_app/models/vis5.html'
topic_count = 5


#### functions ####
def get_medication_name(text):
    
    first_sentence = text.partition('.')[0]
    name = ' '.join(re.findall(r'\b[A-Z][a-z]+|\b[A-Z]\b', first_sentence))
    
    return name

def get_first_2_sentences(text):

    first_2_sentences = '. '.join(text.split('.')[:2])

    return first_2_sentences

def modify_df(df, list_topic_est):

    # add column for medication name
    df['medication_name'] = df['Introduction'].apply(lambda x: get_medication_name(x))

    # add short summary
    df['short_summary'] = df['Introduction'].apply(lambda x: get_first_2_sentences(x))

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

def get_df_each_topic(df, topic_count):

    list_df = []
    for i in range(topic_count):
        name_df = 'df_topic' + str(i)
        column = 'topic' + str(i)
        name_df = df[df[column] > 0.9]
        list_df.append(name_df)

    return list_df



#### app ####
def app():

    st.title('Information on medications')

    ## display trained LDA model ##
    st.header('Topic Model (LDA) trained on drug descriptions text')

    with open(visualization_path, 'r') as f:
        html_string = f.read()
    components.v1.html(html_string, width=1300, height=800, scrolling=False)

    ## Lists of medications under each specific topic
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

    list_df = get_df_each_topic(df, topic_count)

    ## User select which group of medicine to look into ##

    st.header('Look into each group of medications in detail')
    st.subheader('Based on word choices, the medications are grouped into 5 topics')
    st.write('Topic 1 mainly describes anti-bacterial and antibiotics for the body, and also blood cholesterol-lowering medicines.')
    st.write('Topic 2 mainly describes drugs used to treat high blood pressure, heart conditions, and also describes drugs used to treat mental disorders.')             
    st.write('Topic 3 mainly describes anti-coagulants to prevent or treat heart attack and stroke, and other heart conditions.')
    st.write('Topic 4 is a mix of drugs that treat digestive tract symptoms, acne, skin infections, and also pain medications.')
    st.write('Topic 5 mainly describes anti-bacterial and antibiotics used for airway infections and allergies, and some antifungal medications.')
    st.write('')

    list_topics = ['Topic 1', 'Topic 2', 'Topic 3', 'Topic 4', 'Topic 5']
    topic_of_interest = st.selectbox('Look for medications that predominantly belong to 1 of the topics:',
                                     list_topics)
    st.write('Medications that are predominantly ', topic_of_interest)
    
    map_topic_df = {'Topic 1': list_df[0],
                    'Topic 2': list_df[1],
                    'Topic 3': list_df[2],
                    'Topic 4': list_df[3],
                    'Topic 5': list_df[4]}

    list_toshow = map_topic_df[topic_of_interest]['short_summary'].tolist()
    for i in list_toshow:
        st.markdown("- " + i)

    



    
    






if __name__ == '__main__':
    app()