import streamlit as st

# Streamlit App for a Simple Calculator
st.title("Simple Calculator")

# Select the operation
operation = st.selectbox(
    "Select an operation:",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Input numbers from the user
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Perform the calculation when the button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"{num1} / {num2} = {result}")
        else:
            st.error("Error! Division by zero.")
