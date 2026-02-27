import streamlit as st


st.set_page_config(page_title="Calculator App", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #B5838D ;
    }
     h1 { 
            text-align : center;
            color : white !important;
            }
     h3 { 
            text-align: center;
            color :white  !important;
            }
    div.stButton>button:first-child{
            background-color:#D8A7B1;
            color:white;
            border-radius;15px;
            height:3em;
            width:100%
            font-size: 18px;
            border:none;
            }
    div.stButton>button:first-child:hover{
          background-color:#C98A9E;
            }
    .result-box{
            padding:15px
            background-color:white;

            border-radius:10px;
            text-align: center;
            font-weight:bold;
            margin-top:20px;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.08);

            }
    </style>
""", unsafe_allow_html=True)






def calculator():
    
    st.markdown("<h1> Smart calculator </h1>" , unsafe_allow_html=True) 
    st.markdown("<h3> Simple and Decorative Calculator  </h3>" , unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number")
    with col2:
        num2 = st.number_input("Enter second number")

    
    operation = st.selectbox(
        "Choose operation:",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )
    result = None
    if st.button(" Calculate"):
    

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero!")
            
    if  result is not None:          
     st.markdown (
         f"<div class ='result-box'>Result:{result}</div>", 
                   unsafe_allow_html=True
     )    
  
if __name__ == "__main__":
    calculator()