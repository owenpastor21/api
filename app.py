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
        # Hide all Streamlit elements for API calls
        st.set_page_config(initial_sidebar_state="collapsed")
        hide_streamlit_elements = """
            <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                .stDeployButton {display: none;}
                .stToolbar {display: none;}
                .stMarkdown {display: none;}
                .stException {display: none;}
                div[data-testid="stSidebarNav"] {display: none;}
                .stApp {background-color: white;}
                .appview-container {margin: 0; padding: 0;}
            </style>
        """
        st.markdown(hide_streamlit_elements, unsafe_allow_html=True)
        
        function_name = query_params["function"][0]
        try:
            a = float(query_params.get("a", [0])[0])
            b = float(query_params.get("b", [0])[0])
            
            if function_name == "add":
                result = add_numbers(a, b)
                st.write({"result": result})
            elif function_name == "multiply":
                result = multiply_numbers(a, b)
                st.write({"result": result})
            elif function_name == "raw":
                result = get_raw_result(a, b)
                st.write(result)
            else:
                st.error("Unknown function")
            return
        except ValueError:
            st.error("Invalid number format")
            return

    # Regular UI code here
    st.title("Function Hub")
    
    st.header("API Documentation")
    st.markdown("""
    ### How to use the API:
    
    1. **Addition**
    ```
    GET https://yourapp.streamlit.app/?function=add&a=5&b=3
    ```
    
    2. **Multiplication**
    ```
    GET https://yourapp.streamlit.app/?function=multiply&a=4&b=2
    ```
    
    3. **Raw Text**
    ```
    GET https://yourapp.streamlit.app/?function=raw&a=5&b=3
    ```
    
    ### Response Formats:
    - Add/Multiply: JSON response `{"result": number}`
    - Raw: Plain text response
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
