import streamlit as st 
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import SmartDataframe

load_dotenv()


openai_api_key = os.getenv("API_KEY")


def chat_with_csv(df, prompt):
    llm = OpenAI(api_token="API_KEY")
    df = SmartDataframe(df, config={"llm": llm})
    result = df.chat(prompt)
    print(result)
    return result

st.set_page_config(layout='wide')

st.title("ChatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'], accept_multiple_files=True)

if input_csv:
        
        selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csv])
        selected_index = [file.name for file in input_csv].index(selected_file)

        col1, col2 = st.columns([1,1])

        with col1:
            st.info("CSV Uploaded Successfully")
            data = pd.read_csv(input_csv[selected_index])
            st.dataframe(data, use_container_width=True)

        with col2:

            st.info("Chat Below")
            
            input_text = st.text_area("Enter your query")

            if input_text:
                if st.button("Chat with CSV"):
                    st.info("Your Query: "+input_text)
                    result = chat_with_csv(data, input_text)
                    st.success(result)

