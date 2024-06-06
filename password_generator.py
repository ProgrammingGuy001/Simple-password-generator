import streamlit as st
import string
import random
count=0
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)
numbers = ["1","2","3","4","5","6","7","8","9"]
special_characters = ["@","!","#","%","&","*",]
list_of_option=[]
st.title("Password Generator 🔐")
st.subheader("Securing you everyday ❤️")
n= st.slider("Enter the length of the password", 2, 100)
col1, col2, col3 , col4 = st.columns(4)
with col1:
    if st.checkbox("Special characters"):
        list_of_option.append(special_characters)

with col2:
    if st.checkbox("Capital letters"):
        list_of_option.append(uppercase_alphabets)

with col3:
    if st.checkbox("Small letters"):
        list_of_option.append(lowercase_alphabet)

with col4:
    if st.checkbox("Numbers"):
        list_of_option.append(numbers)
                
if st.button("Generate"):
    if list_of_option == []:
        st.error("Choose at least one option")
    else:
        password = "".join(random.choice(random.choice(list_of_option)) for _ in range(n))
        st.success(password.strip())

    

