import streamlit as st

def calculator(num1, num2, operator):
  """
  Performs basic arithmetic operations.

  Args:
    num1: The first operand.
    num2: The second operand.
    operator: The operator to perform (+, -, *, /).

  Returns:
    The result of the operation.
  """

  if operator == '+':
    result = num1 + num2
  elif operator == '-':
    result = num1 - num2
  elif operator == '*':
    result = num1 * num2
  elif operator == '/':
    if num2 == 0:
      raise ValueError("Cannot divide by zero.")
    result = num1 / num2
  else:
    raise ValueError("Invalid operator.")

  return result

# Streamlit app
st.title("Simple Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])

if st.button("Calculate"):
  try:
    result = calculator(num1, num2, operator)
    st.success(f"Result: {result}")
  except ValueError as e:
    st.error(str(e))
