import streamlit as st

def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit app
st.title("BMI Calculator")

# Get user input for weight and height
weight = st.number_input("Enter your weight in kilograms:", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height in meters:", min_value=0.0, format="%.2f")

if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is: {bmi:.2f}")
    st.write(f"You are classified as: {bmi_category(bmi)}")
else:
    st.write("Please enter valid positive numbers for weight and height.")
