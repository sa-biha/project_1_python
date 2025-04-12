import streamlit as st
import random
import datetime

# --- Daily Challenges ---
challenges = [
    "Write down 3 things you're grateful for.",
    "Try something new that scares you a little.",
    "Compliment someone today.",
    "Learn from a mistake you made recently.",
    "Spend 10 minutes journaling about your goals.",
    "Read something inspiring for 15 minutes."
]

# --- Motivational Quotes ---
quotes = [
    "Mistakes are proof you are trying.",
    "Challenges are opportunities to grow.",
    "Small steps every day lead to big results.",
    "Your mindset determines your future.",
    "You can learn anything you set your mind to."
]

# --- Streamlit Page Settings ---
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align: center;'>🌱 Growth Mindset Challenge</h1>", unsafe_allow_html=True)
st.write("Unlock your potential, one day at a time!")

# --- Today's Challenge ---
today = datetime.date.today()
st.markdown(f"### 📅 Today's Challenge ({today})")

# Select challenge based on date so it’s consistent each day
index = today.toordinal() % len(challenges)
st.success(challenges[index])

# --- Daily Affirmation ---
st.markdown("### ✨ Daily Affirmation")
st.info(random.choice(quotes))

# --- Completion Tracking ---
if "completed" not in st.session_state:
    st.session_state.completed = False

completed_today = st.checkbox("✅ I completed today's challenge!")

if completed_today and not st.session_state.completed:
    st.session_state.completed = True
    st.balloons()
    st.success("Awesome! You're growing stronger every day! 💪")

# --- Journal Reflection ---
st.markdown("### 📝 Reflect on Your Experience")
response = st.text_area("How did today's challenge make you feel?")

if st.button("📩 Submit Reflection"):
    if response.strip():
        st.success("Your reflection has been recorded! (Not really saved yet 😅)")
    else:
        st.warning("Please write something before submitting.")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with sabiha ❤️ using Streamlit</p>", unsafe_allow_html=True)
