import streamlit as st
import google.generativeai as genai
import os
import pandas as pd

key=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

model=genai.GenerativeModel('gemini-2.5-flash-lite')


# Lets create the UI
st.title(':yellow[Healthify] : :blue[Your AI-Powered Personal Health & Wellness Assistant]')
st.markdown('''#### This application will assist you to have a better and healthy life.You can ask your health related questions and get pesonalized advice''')

st.sidebar.header(':blue[Enter Your Details]')

tips='''Follow the steps - 
* Enter your details in the side bar
* Enter your gender, age, height(cms) and weight(Kgs)
* Select the number on the fitness scale(0-5) where 5 is fittest and 0 is not fit at all
* After filling the details, write your prompt here and get personalized response'''
st.write(tips)

# Lets configure sidebar

name=st.sidebar.text_input('Enter your name')
gender=st.sidebar.selectbox('Select your gender',['Male','Female','Other'])
age=st.sidebar.text_input('Enter your age in years')
height=st.sidebar.text_input('Enter your height in centimeters')
weight=st.sidebar.text_input('Enter your weight in kilograms')
smoking = st.sidebar.selectbox('Smoking Habit', ['Yes','No'])
alcohol = st.sidebar.selectbox('Drinking Habit', ['Yes','No'])
bmi=pd.to_numeric(weight)/((pd.to_numeric(height)/100)**2)
fitness=st.sidebar.slider('Rate your fitness between 0 and 5',0,5,step=1)
st.sidebar.write(f'{name}, your BMI is : {round(bmi,2)} kg/m^2')

# Using GenAI model to mget the output

user_query=st.text_input('Enter your question here :')
prompt=f"""
You are a professional health and wellness expert with knowledge in nutrition, fitness, lifestyle habits, and preventive care. 
Your task is to provide **personalized, clear, and structured advice** to the user based on their details and query.

User details:
- Name: {name}
- Gender: {gender}
- Age: {age} years
- Height: {height} cm
- Weight: {weight} kg
- BMI: {bmi} kg/m^2
- Fitness rating (0-5): {fitness}
- Smoking habit: {smoking}
- Alcohol habit: {alcohol}

Instructions:
1. Start with a **friendly, empathetic comment** on the user’s overall health based on the details provided.
2. **Analyze the user’s query** and clearly identify the underlying problem or concern.
3. Explain **possible reasons** for the problem.
4. Provide **actionable solutions**, lifestyle changes, or exercises that the user can implement.
5. Suggest which **medical specialist** to consult if necessary.
6. Recommend **habit adjustments** (e.g., reduce smoking/alcohol, improve sleep, etc.) for better health.
7. Provide a **personalized diet plan** in a **table format** with meals, timings, and portion suggestions.
8. Use a **mix of paragraphs, bullet points, and tables** for clarity.
9. **Do not recommend any medication**, even if asked.
10. End with a **concise summary** of all advice for the user to easily follow.

User’s query: {user_query}
"""



if user_query:
    response=model.generate_content(prompt)
    st.write(response.text)