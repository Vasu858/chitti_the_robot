import streamlit as st
#print welcome to gen ai and agent ai course in bold and center
st.markdown("<h1 style='text-align: center; color: blue;'>Welcome to GEN AI and AGENT AI Couse</h1>", unsafe_allow_html=True)
st.write("Please enter your details to register for the course")    

#give me a button that ask user enter you name and when enterned print he name      use text_input and button

name = st.text_input("Enter your name")
if st.button("Enter", key="enter_name"):
    st.write(f"Hello {name}")

#give me select box that ask user to select their gender and when selected print the gender
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
if st.button("Enter", key="enter_gender"):
    st.write(f" {gender}")

#give me radio buttion that ask your qualification like btech, mtech, phd and when selected print the qualification
qualification = st.radio("Select your qualification", ["Btech", "Mtech", "Phd"])
if st.button("Enter", key="enter_qualification"):
    st.write(f"{qualification}")

#give a submit button . when user clicking then it will display we have registed to gen ai and agent ai course  . give a button that ask user to enter their email and when entered print the email
if st.button("Submit", key="submit_registration"):
    st.write("you have registed to gen ai and agent ai course")






