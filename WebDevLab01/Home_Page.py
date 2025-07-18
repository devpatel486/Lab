import streamlit as st

# Title and subtitle
st.title("Dev Patel -- CS 1301")
st.subheader("Hey! This is my Website and all my hobbies I'm interested in!!! \n Click on the different emojis to take you different pages!")

"\n"

# Pages with their descriptions
## might make it interactive by clicking on the the icon 


##NEW  ##user input
st.page_link("pages/1_Portfolio.py", label = "***Portfolio***: A portfolio page that showcases my many skills, past experiences and connections.", icon = "💼")
"\n"
st.page_link("pages/2_Current_Hobbies.py", label = "***Current Hobbies***: \n A page that displays about my current hobbies.", icon = "📈")
"\n"


"\n"

st.header("Where I'm from 🏠")
st.image("images/Thomasville.jpeg")
