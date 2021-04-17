import streamlit as st
import sqlite3
import pandas as pd
from what import call
import streamlit.components.v1 as components
    
    
connection = sqlite3.connect('temp.db')

dep = st.selectbox('',('EC', 'IT', 'EEE', 'ME', 'CE',))

sem = st.selectbox('',('1', '2', '3', '4', '5','6', '7','8'))

sub = st.selectbox('',('comp', 'phy', 'chem', 'math', 'english',))



if st.button('Take attendance'):
    
    with open("./classes/{}.csv".format(dep+sem+sub),"w") as f:
        f.write('F_name,L_name,chat_id')
        f.close()
    
    call(dep,sem,sub)
    
       
    

    



    

