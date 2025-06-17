import streamlit as st
import requests

st.title("📝 AI Blog Generator")

topic = st.text_input("Enter your blog topic:")
if st.button("Generate"):
    res = requests.post("http://127.0.0.1:5000/generate", json={"topic": topic})
    if res.status_code == 200:
        st.text_area("Generated Blog:", res.json()['blog'], height=400)
    else:
        st.error("Failed to generate blog.")