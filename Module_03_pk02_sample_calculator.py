import streamlit as st

def calculator(num1, num2, operator):
  """
  Performs basic arithmetic operations.

  Args:
    num1: The first operand.
    num2: The second operand.
    operator: The operator to perform (Add, Subtract, Multiply, Divide, Integer Divide).

  Returns:
    The result of the operation.
  """

  if operator == "Add":
    result = num1 + num2
  elif operator == "Subtract":
    result = num1 - num2
  elif operator == "Multiply":
    result = num1 * num2
  elif operator == "Divide":
    if num2 == 0:
      raise ValueError("Cannot divide by zero.")
    result = num1 / num2
  elif operator == "Integer Divide":
    if num2 == 0:
      raise ValueError("Cannot divide by zero.")
    result = num1 // num2
  else:
    raise ValueError("Invalid operator.")

  return result

# Streamlit app
st.title("Simple Calculator")

num1 = st.number_input("Enter the first number", format="%f")
num2 = st.number_input("Enter the second number", format="%f")

operator = st.selectbox("Select an operator", ["Add", "Subtract", "Multiply", "Divide", "Integer Divide"])

if st.button("Calculate"):
  try:
    result = calculator(num1, num2, operator)
    st.success(f"Result: {result}")
  except ValueError as e:
    st.error(str(e))
