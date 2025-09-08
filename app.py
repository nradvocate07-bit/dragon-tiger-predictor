import streamlit as st
import random

st.title("Dragon Tiger Predictor (Demo Version)")

# Track balance
if "balance" not in st.session_state:
    st.session_state.balance = 1000

# User inputs
round_number = st.number_input("Enter Round Number:", min_value=1, step=1)
choice = st.selectbox("Your Choice:", ["Dragon", "Tiger"])

# Simple random prediction
prediction = random.choice(["Dragon", "Tiger"])
confidence = round(random.uniform(50, 100), 2)

# Betting suggestion
if confidence > 70:
    suggestion = "Bet Normal"
elif confidence > 60:
    suggestion = "Bet Double"
else:
    suggestion = "Skip"

# Display results
st.subheader("Prediction")
st.write(f"Predicted Winner: **{prediction}**")
st.write(f"Confidence: {confidence}%")
st.write(f"Betting Advice: {suggestion}")

# Balance update (demo only)
if st.button("Play Round"):
    if choice == prediction:
        st.session_state.balance += 100
        st.success("You Won! +100")
    else:
        st.session_state.balance -= 100
        st.error("You Lost! -100")

st.write(f"💰 Current Balance: {st.session_state.balance}")
