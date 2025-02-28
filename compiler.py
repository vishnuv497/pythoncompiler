import streamlit as st
import sys
import io

def execute_code(code):
    """Executes the provided Python code and captures output."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        exec(code, {})  # Execute code in an isolated scope
        output = sys.stdout.getvalue()
    except Exception as e:
        output = str(e)
    
    sys.stdout = old_stdout  # Restore original stdout
    return output

# Streamlit UI
st.title("Python Code Compiler")
st.write("Enter your Python code below and click Run.")

# Code input
code = st.text_area("Write your Python code here:", height=200)

if st.button("Run Code"):
    result = execute_code(code)
    st.text_area("Output:", result, height=200, disabled=True)
