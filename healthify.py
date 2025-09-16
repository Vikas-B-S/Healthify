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
prompt=f'''Assume you are the health and diet expert.You are required to answer the question asked by the user.
Use the following details provided by the user.
name of the user is {name}
gender is {gender}
age is {age}
weight is {weight} kgs
height is {height} cms
BMI is {bmi} kg/m^2
and user rates his/her fitness as {fitness} out of 5

Your output should be in the following format 
* It should start by giving one or two line comment on the details that have been given by user.
* It should explain what the real problem is based on the query asked by the use.
* What could be the possible reason for the problem.
* What are the possible solutions for the problem.
* You can also mention which doctor should the user consult (specialization) if required.
* Suggest whether the user must quit few habits for a better life.
* Suggest a diet plan to the user as per the details and query provided by the user, this can be in a table. 
* Strictly don not recommend or advise any medication, even if it is been asked by user.
* output should be in both paragraph, bullet point and use tables wherever it is required.
* In the end give me summary of everything that has been discussed

Here is the query from the user {user_query}'''


if user_query:
    response=model.generate_content(prompt)
    st.write(response.text)