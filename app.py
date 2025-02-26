import streamlit as st
from scraper import extract_text_from_url
from qa import QASystem

st.title("Web Content Q&A Tool")

# User input: URLs
urls = st.text_area("Enter URLs (one per line):")

if st.button("Ingest Content"):
    urls = urls.split("\n")
    content = ""

    with st.spinner("Fetching content..."):
        for url in urls:
            text = extract_text_from_url(url.strip())
            content += text + "\n\n"

    if content.strip():
        st.session_state["qa_system"] = QASystem(content)
        st.success("Content ingested successfully!")
    else:
        st.error("Failed to extract content from the given URLs.")

# User input: Question
question = st.text_input("Ask a question:")

if st.button("Get Answer") and "qa_system" in st.session_state:
    answer = st.session_state["qa_system"].answer_question(question)
    st.write("**Answer:**", answer)
elif not "qa_system" in st.session_state:
    st.warning("Please ingest content first.")
