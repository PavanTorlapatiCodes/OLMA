import streamlit as st
from ollama import Client

# ✅ Create client instance (VERY IMPORTANT)
client = Client(host="http://localhost:11434")

st.set_page_config(
    page_title="Custom LLM model by Pavan Torlapati - Ollama",
    layout="centered"
)

st.title("Mr. Pavan Torlapati - Ollama App")

prompt = st.text_area("Enter your prompt:", height=200)

if st.button("Generate Response"):
    if prompt.strip() == "gemma3:270m":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="gemma3:270m",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("Response Generated!")
            st.write(response["message"]["content"])