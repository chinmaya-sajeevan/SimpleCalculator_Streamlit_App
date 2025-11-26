
import streamlit as st

#Set the title of the streamlit app
st.title("Simple Calculator")

#Create a selectbox for arithmetic operation
operation=st.selectbox("Select an operation",options=("+","-","*","/"))

#Input numbers
num1=st.number_input("Enter the first number",value=0.0)
num2=st.number_input("Enter the second number",value=0.0)

#Create a button to trigger the calculation
if st.button("Calculate"):
    result = None

    if operation== "+":
        result=num1+num2
    elif operation== "-":
        result=num1-num2
    elif operation== "*":
        result=num1*num2
    elif operation== "/":
        if num2==0:
            st.error("Error:Cannot divide by zero")
        else:
            result=num1/num2

#Display the result if calculation was successfull 
    if result is not None:
        st.success(f"The result is : {result}")



