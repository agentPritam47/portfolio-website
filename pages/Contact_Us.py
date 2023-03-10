import streamlit as st
import send_email

st.title("Contact Me")

with st.form(key="emails_forms"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Your message")
    message = message + "\n" + user_email
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email.mail(message)
        st.info("your email was send successfully")