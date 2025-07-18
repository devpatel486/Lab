import streamlit as st


st.title("These are the current hobbies that I am involved in.")
"\n"

st.header("Investing in the Stock Market💸:")

st.write("I started investing at the age of 14 years-old and I have a high interest in the finance game.")

"\n"
st.write("Here is the current investments I have with my unrealized :green[gains] / :red[losses]:")
st.write("The button below will reveal my current holding, current price, and unrealized lost/gain.")


"\n"
"\n"

# NEW streamlit function: button + metric columns ## static
if st.button("Check me out!"):

    col1, col2, col3 = st.columns(3)
    col1.metric("Tesla", "$319", "-$427")
    col2.metric("Google", "$183", "$45")
    col3.metric("Palantir", "$154", "$145")


import json
import pandas as pd

with open("data.json") as f:
    prices = json.load(f)

st.header("Below can allow you to move the slider based on how many shares you have -- giving you the current portfolio cost.")
st.subheader("📈 Portfolio Visualizer: Adjust Your Shares")
st.write("Use the sliders below to choose how many shares you own of each stock.")

# Session state for  shares
for stock in prices:
    if f"{stock}_shares" not in st.session_state:
        st.session_state[f"{stock}_shares"] = 0

# Sliders for each stock  ## dynamic
tesla = st.slider("Tesla Shares", 0, 20, st.session_state["Tesla_shares"])  # NEW
google = st.slider("Google Shares", 0, 20, st.session_state["Google_shares"])  # NEW
palantir = st.slider("Palantir Shares", 0, 20, st.session_state["Palantir_shares"])  # NEW

# Update session state
st.session_state["Tesla_shares"] = tesla
st.session_state["Google_shares"] = google
st.session_state["Palantir_shares"] = palantir

# values
values = {
    "Tesla": tesla * prices["Tesla"],
    "Google": google * prices["Google"],
    "Palantir": palantir * prices["Palantir"]
}

# bar chart
st.subheader("📊 Portfolio Value by Stock")
df = pd.DataFrame.from_dict(values, orient="index", columns=["Total Value"])
st.bar_chart(df)


portfolio_values = [6800, 6900, 6200, 5600, 5800, 6800, 7100]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

# Build a DataFrame with labels
df = pd.DataFrame({
    "Month": months,
    "Portfolio Value $": portfolio_values
})

# Set Month as index so it appears on X-axis
df = df.set_index("Month")

st.subheader("📈 YTD Portfolio Value ")
st.write("This will show the graph of my portfolio throughout this year:")
st.line_chart(df)



"\n"

import streamlit as st

st.title("📸 Photography")
st.write("Here are some of the photos I've taken in high school:")

# 4 photos
st.image("images/pic1.png")
st.image("images/pic2.png")
st.image("images/pic3.png")
st.image("images/pic4.png")

st.header("⭐ Rate these pictures as a collective whole")


sentiment_mapping = ["one", "two", "three", "four", "five"]


rating_index = st.slider("Rate these photos (1–5 stars):", 1, 5, key="photo_rating")
rating_word = sentiment_mapping[rating_index - 1]  

st.markdown(f"You selected **{rating_word}** star(s).")

# balloons 
if rating_index == 5:
    st.balloons()





