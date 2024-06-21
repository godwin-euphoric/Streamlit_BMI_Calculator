import streamlit as st

st.title("BMI Calculator")
st.write("This app calculates your Body Mass Index (BMI) based on your height and weight.")

weight=st.number_input("Enter your weight (kg):",min_value=0.0)
height=st.number_input("Enter your Height (m):", min_value=0.0,step=0.01)

#Step argument controls the increment/decrement amount when using the up/down arrows or clicking on the number input field in the Streamlit app.

if weight>0 and height>0 :
    bmi=weight/(height*height)
    st.write("Your BMI is :", bmi)
    if bmi <18.5 : 
        st.write("You are Underweight")
    elif bmi < 25:
        st.write("You are normal weight.")
    elif bmi < 30:
        st.write("You are overweight.")
    else:
        st.write("You are obese")
else:
    st.write("Enter Positive Values for Weight and Height")



