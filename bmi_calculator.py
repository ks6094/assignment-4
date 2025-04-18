import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)

# Streamlit app
st.title("BMI Calculator")

st.header("Enter your details:")
# Get user input for weight and height
weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Height (m):", min_value=0.1, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.info("You are overweight.")
        else:
            st.info("You are obese.")
    else:
        st.warning("Please enter valid weight and height values.")