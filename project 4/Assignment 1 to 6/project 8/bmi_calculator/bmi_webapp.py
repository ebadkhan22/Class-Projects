import streamlit as st

# Function to calculate BMI
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    if height_m <= 0:
        return 0
    return round(weight_kg / (height_m ** 2), 2)

# Function to determine BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit app
def main():
    st.set_page_config(page_title="BMI Calculator", layout="centered")
    st.title("🧮 BMI Calculator Web App")
    st.write("Enter your height and weight to calculate your BMI:")

    height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0, step=1.0)
    weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=300.0, step=1.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)

        st.success(f"Your BMI is **{bmi}**")
        st.info(f"You are categorized as: **{category}**")

        if category == "Underweight":
            st.warning("⚠️ Consider eating more nutritious food.")
        elif category == "Obesity":
            st.warning("⚠️ Consult a healthcare provider for advice.")

if __name__ == "__main__":
    main()
