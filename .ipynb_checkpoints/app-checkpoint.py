import streamlit as st
from utils import extract_text_from_pdf
from llama_config import ask_llama

st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("📄 Chat with Your PDF using LLaMA")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Extracting PDF content..."):
        text = extract_text_from_pdf(uploaded_file)
        st.success("PDF uploaded and text extracted!")

    st.markdown("### Ask a question based on the PDF:")
    question = st.text_input("Your question")

    if question:
        with st.spinner("Thinking..."):
            prompt = f"Answer the following question based on this PDF content:\n\n{text[:5000]}\n\nQuestion: {question}"
            answer = ask_llama(prompt)
            st.markdown("### 🧠 Answer:")
            st.write(answer)
