import streamlit as st
import google.generativeai as genai


#css
st.markdown(
    """
    <style>
        body {
            background-color: #2E3440;
            color: #D8DEE9;
        }
        textarea {
            background-color: #3B4252 !important;
            color: #ECEFF4 !important;
        }
        .stButton>button {
            background-color: #5E81AC;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #81A1C1;
        }
    </style>
    """,
    unsafe_allow_html=True
)






genai.configure(api_key="AIzaSyClPMgcsZPQppE9_BZTCZbmAWojvvxpLo4")

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

system_prompt = """ Consider yourself as a code reviewer and assist with the error that can occur .
you can also help me build code using the prompt.
respectfully reject the request that are not related to coding or similar activities.
also expalin the code bugs or errors done by the user and give an explaination for that
main job is to analyze the submitted code and identify potential bugs, errors and/or areas of improvement and correct the code.

"""
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash",system_instruction=system_prompt)



# Streamlit app title
st.title("🚀 CodeDoctor: Diagnose & Fix Bugs using ai")

code = st.text_area("✍️ Enter your code here:")



if st.button("Submit"):
    
    
    response = model.generate_content(code)
    st.subheader("🤖 AI Response:")
    # st.write()
    st.markdown(response.text)
    
    
    
    
    


