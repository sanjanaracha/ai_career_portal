import streamlit as st
import requests 

from streamlit_local_storage import LocalStorage

ls=LocalStorage()

se_url=st.secrets["be_url"]
st.title("Welcome ti Job Seeker Dashboard")

file=st.file_uploader("choose",type=["pdf"])
college_name=st.text_input("enter college name")
passedout_year=st.number_input("enter passedout_year")
cgpa=st.number_input("enter cgpa")
expected_jobs=st.selectbox("choose",["frontend Developer","Data Analyst","Software Tester","Backend Developer","GenAI Developer","Data Science"])
logged_user=ls.getItem("logged_user")
# st.write(logged_user)
user_id=logged_user["id"]
st.write(user_id)


if st.button("Upload"):

    if file:
        data={
           "user_id":user_id,
           "college_name":college_name,
           "passedout_year":passedout_year,
           "cgpa":cgpa,
           "expected_jobs":expected_jobs
        }


        response=requests.post(f"{se_url}/resume_upload",
                            files={
                            "file": (
                            file.name,
                            file.getvalue(),
                            "application/pdf"
                            )
                            },data=data)
        st.write(data)
        st.write(file.name)
        # st.write(response)
        st.write("Status:", response.status_code)
        st.write("Response Text:", response.text)


