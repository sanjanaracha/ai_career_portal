from streamlit_local_storage import LocalStorage
import streamlit as st
import requests as r
ls = LocalStorage()

b_url="http://127.0.0.1:8000"

user = ls.getItem("logged_user")

st.title("Welcome to Recruiter Dashboard")
photo=st.file_uploader("image",type=["png","jpg","jpeg"])
exp=st.number_input("experience")
company=st.text_input("company")
        # if photo is not None:
        #     st.image(photo,caption="uploaded image",use_container_width=True)

p_r_sub_btn=st.button("Submit")

if p_r_sub_btn:
            # payload={
            #     "exp":exp,
            #     "company":company
            # }
    files = {
    "file": (
        
    photo.name,
    photo.getvalue(),
    photo.type

    )
    }

    data = {
    "exp": exp,
    "company": company,
    "pic_id": user["id"]
    }
    res=r.post(f"{b_url}/profile_recruiter",data=data,files=files)
    st.write(res)