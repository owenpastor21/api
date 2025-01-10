import streamlit as st
from urllib.parse import parse_qs

def add_numbers(a: float, b: float) -> float:
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    return a * b

def get_raw_result(a: float, b: float) -> str:
    return f"The numbers are {a} and {b}"

def main():
    # Handle URL parameters
    query_params = st.experimental_get_query_params()
    
    if "function" in query_params:
        function_name = query_params["function"][0]
        try:
            a = float(query_params.get("a", [0])[0])
            b = float(query_params.get("b", [0])[0])
            
            if function_name == "add":
                result = add_numbers(a, b)
                st.json({"result": result})
            elif function_name == "multiply":
                result = multiply_numbers(a, b)
                st.json({"result": result})
            elif function_name == "raw":
                result = get_raw_result(a, b)
                st.text(result)  # This will return plain text instead of JSON
            else:
                st.error("Unknown function")
            return
        except ValueError:
            st.error("Invalid number format")
            return
    
    st.title("Function Hub")
    
    st.header("Available Functions")
    st.markdown("""
    ### 1. Addition
    Adds two numbers together
    
    ### 2. Multiplication
    Multiplies two numbers together
    """)
    
    # Test section
    st.header("Test Functions")
    
    with st.expander("Test Addition"):
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Enter first number (a)", key="add_a")
        with col2:
            b = st.number_input("Enter second number (b)", key="add_b")
        if st.button("Calculate Addition"):
            result = add_numbers(a, b)
            st.success(f"Result: {result}")
            
    with st.expander("Test Multiplication"):
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Enter first number (a)", key="mult_a")
        with col2:
            b = st.number_input("Enter second number (b)", key="mult_b")
        if st.button("Calculate Multiplication"):
            result = multiply_numbers(a, b)
            st.success(f"Result: {result}")

    # Add new section to UI
    with st.expander("Test Raw Output"):
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Enter first number (a)", key="raw_a")
        with col2:
            b = st.number_input("Enter second number (b)", key="raw_b")
        if st.button("Get Raw Output"):
            result = get_raw_result(a, b)
            st.code(result)

if __name__ == "__main__":
    main()
