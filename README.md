# Streamlit app to showcase the use of Natural Language Processing techniques in solving business problems

This project started out as a collection of Natural Language Processing techniques that can be used to solve business problem such as matching social media text to different business categories.

One method is topic modeling by Latent Dirichlet Allocation (LDA), which count words, detects word frequencies, and compare their distributions across documents. This process can discover hidden topics among documents, and deduce topic distributions for each document.
For this model, I used the [gensim](https://radimrehurek.com/gensim/intro.html#what-is-gensim) library, which is a popular NLP library for topic modeling. Another python NLP package used is [NLTK :: Natural Language Toolkit](https://www.nltk.org). It provides a range of tools for text preprocessing for the English language.


## How to run

At root directory, run app by typing
`streamlit run app.py`

## Requirements

Python libraries listed in requirements.txt file.

Also need to download nltk libraries:
1. WordNet - lexical database of English, for lemmatization step in text preprocessing
2. Stopwords - for removing stop words during text preprocessing

