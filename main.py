# Importing our web app library
import streamlit as st

# Adjusting the layout of our webpage to look better
st.set_page_config(layout="wide")

# Creating two columns to organize our information
col1, col2 = st.columns(2)

# Displaying our Photo
with col1:
    st.image("images/PHOTO.jpg", width=300)

# Display our initial text
with col2:
    st.title("Juan Carlos Cabrera")
    content = """
    Hello! I'm Juan Carlos. I'm a recent Software Engineering graduate aiming to leverage my abilities to successfully become a reliable member of a software engineering team. 
    I look forward to potentially working with you!
"""
    st.info(content)

content2 = """
Below you can find some of the apps I've created after graduation. 
Previous projects are on my GitHub; access granted upon request.
Feel free to contact me!
"""
st.write(content2)