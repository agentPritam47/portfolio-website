import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, emptycol, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("photos/catto.png")

with col2:
    st.title("Pritam Das")
    content = """hello there i am pritam a python programmer, currently studing at JIS College
    My stream is computer science engineering. I live in a beautiful city named kanchrapara which is located at wesbengal in India.
    I love to create such things that help people in their day to day life."""
    st.info(content)

info = """
Below you can find some apps i have built in python. Feel free to contact me!
"""
st.header(info)
col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("photos/" + rows["image"])
        st.write(f"[source code] = upcoming")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows["title"])
        st.write(rows["description"])
        st.image("photos/" + rows["image"])
        st.write(f"[source code] = upcoming")
