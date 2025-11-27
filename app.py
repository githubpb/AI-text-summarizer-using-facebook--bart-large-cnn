import streamlit as st
from src.summarizer import TextSummarizer

st.set_page_config(page_title="AI text summarizer", layout="centered")

st.title("📝 AI Text Summarizer")
st.write("Built with BART transformer model")

text = st.text_area("Enter text to summarize", height=250)
min_len = st.slider("Minimum summary length", 20, 200, 40)
max_len = st.slider("Maximum length summary", 50, 400, 100)

if st.button("Summarize"):
    if len(text.strip()) == 0:
        st.error("please enter text to summarize")
    else:
        summarizer = TextSummarizer(model_name="facebook/bart-large-cnn")
        summary = summarizer.summarizer(text, min_len, max_len)
        st.subheader("Summary: ")
        st.write(summary)
