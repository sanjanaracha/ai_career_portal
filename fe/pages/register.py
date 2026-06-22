import streamlit as st

import requests

st.title("Register")
s_url=st.secrets["be_url"]

with st.form("register..."):
    name=st.text_input("name")
    email=st.text_input("email")
    password=st.text_input("password",type="password")
    role=st.selectbox("choose:",["Recruiter","JobSeeker"])
    register_btn=st.form_submit_button("Register")
    login_btn=st.form_submit_button("Login")

    if register_btn:
        payload={
            "name":name,
            "email":email,
            "password":password,
            "role":role
        }
        res=requests.post(f"{s_url}/register",json=payload)

        st.write(res)

    if login_btn:
        st.switch_page("pages/login.py")