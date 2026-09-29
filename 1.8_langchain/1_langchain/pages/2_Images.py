from tools.image_gen import generate_image
import streamlit as st

st.title("Ai Image Generation")
prompt = st.text_input("Descripe the image you want to generate")

if st.button("Generate"):
    with st.spinner("Generate..."):
        image = generate_image(prompt)
        st.image(image, caption=prompt, use_container_with=True)