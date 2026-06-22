import streamlit as st
import requests
from streamlit_local_storage import LocalStorage
st.title("Login")

ls=LocalStorage()
s_url=st.secrets["be_url"]

with st.form("login.."):
    email=st.text_input("email")
    password=st.text_input("password")
    role=st.selectbox("choose:",["Recruiter","JobSeeker"])
    login_btn=st.form_submit_button("Login")

    if login_btn:
        payload={
            "email":email,
            "password":password,
            "role":role
        }
        res=requests.post(f"{s_url}/login",json=payload)
        data=res.json()["xyz"]
        st.write("Status Code:", res.status_code)
        st.write("Response Text:", res.text)
        st.write(data[0])
    
        if isinstance(data,list):
            ls.setItem("logged_user",data[0])
            l_user=ls.getItem("logged_user")
            # l_email=l_user["email"]
            l_role=l_user["role"]
            st.write("Saved:", data[0])
            st.write("GET:", ls.getItem("logged_user"))

            # st.stop()

            if l_role=="Recruiter":
                st.switch_page("pages/R_Dashboard.py")
            elif l_role=="JobSeeker":
                st.switch_page("pages/J_dashboard.py")
        if isinstance(data,str):
            st.write(data)

