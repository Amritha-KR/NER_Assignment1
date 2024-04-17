import streamlit as st
import spacy
from newspaper import Article
from spacy import displacy
#from collections import counter
import en_core_web_sm
nlp=en_core_web_sm.load()
from pprint import pprint
st.title("NER Demo")

url=st.text_input("Enter URL")
st.write("OR")

text=st.text_area("Enter paragraph")

if(st.button("Analyze")):
    if text and url:
        st.write("please enter either URL or Text to analyze")
    elif text:

        doc=nlp(text)
        ent_html=displacy.render(doc,style="ent",jupyter=False)
        #display the entity visualization in the browser:
        st.markdown(ent_html,unsafe_allow_html=True)
    elif url:

        try:
            article=Article(url)
            article.download()
            article.parse()
            url_text=article.text
            doc=nlp(url_text)
            ent_html=displacy.render(doc,style="ent",jupyter=False)
            st.markdown(ent_html,unsafe_allow_html=True)
        except Exception as e:
            st.write("PLease enter valid URL")
    else:
        st.write("please enter URL or Text to analyze")

        