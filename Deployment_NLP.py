import pandas as pd
import numpy as np
import streamlit as st

import re
import contractions

import nltk
import string
from nltk import punkt, tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from PIL import Image

from textblob import TextBlob
#from sklearn.feature_extraction.text import TfidfVectorizer

#from sklearn.svm import SVC
#import pickle


def main():

    image = Image.open(r"D:\Downloads\NLP_project\image.jpg")
    st.image(image)


    st.header("Hotel Reviews-Sentimental analysis")
    st.write("Our major objective is what are the attributes that travelers are considering while selecting a hotel. With this manager can understand which elements of their hotel influence more in forming a positive review or improves hotel brand image.")
    
    
    input_text = st.text_area("𝐓𝐲𝐩𝐞 𝐫𝐞𝐯𝐢𝐞𝐰 𝐡𝐞𝐫𝐞", height=150)

    option = st.sidebar.selectbox('Menu bar',['Key words','Sentiment Analysis',])

    if option == "Key words":

        if st.button("Key words"):
            my_stop_words = stopwords.words('english')
            my_stop_words.remove('not')

            lemmatizer = WordNetLemmatizer()

            text = re.sub('\w*\d\w*','',input_text)
            text = contractions.fix(text)
            text = "".join([i for i in text if i not in string.punctuation])
            text = text.lower()
            text = word_tokenize(text)
            text = [i for i in text if i not in my_stop_words]
            text = [lemmatizer.lemmatize(word) for word in text]

            st.write(text)


    else:
    
        if st.button("Sentiment Analysis"):
    
            my_stop_words = stopwords.words('english')
            my_stop_words.remove('not')

            lemmatizer = WordNetLemmatizer()

            text = re.sub('\w*\d\w*','',input_text)
            text = contractions.fix(text)
            text = "".join([i for i in text if i not in string.punctuation])
            text = text.lower()
            text = word_tokenize(text)
            text = [i for i in text if i not in my_stop_words]
            text = [lemmatizer.lemmatize(word) for word in text]
            text = ' '.join(text)
            
            score = TextBlob(text)

            if score.sentiment.polarity <0:
                st.write(" 𝐍𝐞𝐠𝐚𝐭𝐢𝐯𝐞 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭 😔")
                st.write("Polarity:",score.sentiment.polarity, "Subjectivity:",score.sentiment.subjectivity)
            
            else:
                if score.sentiment.polarity == 0 :
                    st.write(" Neutral Statement 😶")
                    st.write("Polarity:",score.sentiment.polarity, "Subjectivity:",score.sentiment.subjectivity)

                else:
                    st.write("𝐏𝐨𝐬𝐢𝐭𝐢𝐯𝐞 𝐒𝐭𝐚𝐭𝐞𝐦𝐞𝐧𝐭 😃")
                    st.write("Polarity:",score.sentiment.polarity, "Subjectivity:",score.sentiment.subjectivity)

                result_sentiment = blob.sentiment
                st.success(result_sentiment)

if __name__ == "__main__":
     main()

            


