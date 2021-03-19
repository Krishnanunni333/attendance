import streamlit as st


department = st.selectbox('',('EC', 'IT', 'EEE', 'ME', 'CE',))

semester = st.selectbox('',('1', '2', '3', '4', '5','6', '7','8'))



if st.button('Take attendance'):
    import call
    call.calls()
    
    

