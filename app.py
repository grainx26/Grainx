import streamlit as st
import streamlit.components.v1 as components

with open("grainscope.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.set_page_config(page_title="GrainScope", layout="wide")
components.html(html_content, height=1600, scrolling=True)
