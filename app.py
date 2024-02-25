import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, resume_content):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt + '\n' + resume_content)
    return response.text

def input_pdf_setup(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

#Prompt Template

st.set_page_config(page_title="DRAA")
st.header("Dynamic Resume Analysis Application")
input_text = st.text_area("Job Description: ")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Percentage Match")

input_prompt1 = """ACT AS A PROFESSIONAL AND DISCIPLINED HIRING LEAD WHILE COMPARING THE SKILLSET. BE A LITTLE SCRUTINIZING.
Your task as an expert system is to compare the technical skills/skills/projects/required skills/tech stack used,etc section of the candidate's resume with the skills mentioned in the job description provided for a Software Development Internship. Calculate the percentage match between the skills present in the resume and those in the job description.

Begin by extracting the technical skills/skills/projects/required skills/tech stack used,etc section from the candidate's resume and the same details mentioned in the job description.

Next, compare the technical skills/skills/projects/required skills/tech stack used,etc listed in the job description with those present in the candidate's resume.

Identify and count the number of skills that appear in both the job description and the candidate's resume.

Calculate the percentage match by dividing the number of matched skills by the total number of skills mentioned in the job description, then multiplying by 100. This will provide a percentage representing the level of alignment between the skills possessed by the candidate and the requirements of the internship position.

Provide the candidate with the calculated percentage match, indicating how well their resume aligns with the skills specified in the job description.

Your analysis should be accurate and objective
THE PERCENTAGE MATCH SHOULD BE ACCURATE AND ONLY OUTPUT THE MATCH PERCENTAGE with the % 


"""





submit3 = st.button("Tell Me About The Resume")
input_prompt3 = """
I COMMAND YOU TO BE AS STRICT AS POSSIBLE WHILE TELLING ABOUT THE RESUME. SCRUTINIZE EVERY SINGLE DETAIL.
You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.

"""

submit4 = st.button("How Can I Improvise My Skills")
input_prompt4 = """As an expert system, your task is to analyze the candidate's current skills, as outlined in their resume,
and compare them with the requirements specified in the job description.Based on this analysis, provide personalized recommendations to the candidate on how 
they can enhance their skills to better align with the position's requirements.dentify specific areas where the candidate may need further development and suggest 
actionable steps they can take to improve their proficiency in key areas. Your recommendations should be informative, practical, and tailored to the candidate's current 
skill level and career aspirations, aiming to equip them with the necessary expertise to excel in the targeted internship role and beyond.

"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload The Resume")



elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload The Resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload The Resume")
