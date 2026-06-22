from fastapi import FastAPI,UploadFile,File,Form
from database import supabase_c
app=FastAPI()

@app.post("/resume_upload")
async def resume_upload(user_id:str=Form(...),file:UploadFile=File(...),college_name:str=Form(...),passedout_year:int=Form(...),cgpa:float=Form(...),expected_jobs:str=Form(...)):
    file_bytes=await file.read()
    filename=f"{user_id}_{file.filename}"

    res=supabase_c.storage.from_("resumes").upload(
        filename,
        file_bytes)
    print(res)
    url=supabase_c.storage.from_("resumes").get_public_url(filename)
    print(url)
    resume=supabase_c.table("resume").insert({
        "resume_link":url,
        "f_id":user_id,
        "college_name":college_name,
        "passesout_year":passedout_year,
        "CGPA":cgpa,
        "expected_job":expected_jobs
        }).execute()
    return{
        "resume_url":url,
        "msg":"resume uploaded successfully"

    }

@app.post("/profile_recruiter")
async def profile_recruiter_fun(exp:int=Form(...),
                                company:str=Form(...),
                                file:UploadFile=File(...),
                                pic_id:str = Form(...)):
    file_read=await file.read()
    file_name=f"{pic_id}_{file.filename}"

    supabase_c.storage.from_("recruiter_files").upload(file_name,file_read)
    url=supabase_c.storage.from_("recruiter_files").get_public_url(file_name)

    supabase_c.table("recruiter_details").insert({
        "photo":url,
        "experience": exp,
        "company": company,
        "pic_id": pic_id

    }).execute()
    return{
        "resume_url":url,
        "msg":"profile uploaded successfully"

    }





@app.post("/register")
def register(payload:dict):
    res=supabase_c.table("users_agentic").insert(payload).execute()
    return{
        "msg":"user added successful",
        "res_obj":res
    }


@app.post("/login")
def login(payload:dict):
    e=payload["email"]
    p=payload["password"]
    r=payload["role"]
    res=supabase_c.table("users_agentic").select("*").eq("password",p).eq("email",e).eq("role",r).execute()
    

    if len(res.data)==0:
        return{
            "xyz":"no user found"
        }
    else:
        return{
            "xyz":res.data
        }
