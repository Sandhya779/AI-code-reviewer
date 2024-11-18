import streamlit as st
import google.generativeai as genai
import os
api_key = os.environ.get("GOOGLE_GENERATIVE_AI_API_KEY")
genai.configure(api_key=api_key)
llm=genai.GenerativeModel('gemini-1.5-flash')
sys_prompt="""You are an expert AI code reviewer. Your work is to anlayze the code submitted
            by the user by reviewing it i.e. identifying the bugs and displaying the report of the bugs detected,
            helping the user by providing them with the corrected code or the optimized code
            and other required suggestions.
            Maintain a decent conversation while explaining the user .
            Focus on accuracy, efficiency and improving the user's understanding of best coding practices. 
            Kindly decline if the user's input is out of your work.   
            """

def get_response(sys_prompt,code):
    response=llm.generate_content([sys_prompt,code])
    return response.text

st.title("AI Code Reviewer")
code=st.text_area('Your code', placeholder="Please paste your code here!!")
button=st.button("Generate")
if button: 
        response=get_response(sys_prompt,code)
        st.header("Code Review")
        st.write(response)


