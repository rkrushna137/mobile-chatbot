import streamlit as st
from openai import OpenAI
import os

# Get API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Mobile Expert Chatbot", page_icon="📱")

st.title("📱 Mobile Expert Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a mobile phone expert. "
                       "Whenever user asks about a mobile, give details like "
                       "Display, RAM, Storage, Camera, Battery, Processor and Approx Price. "
                       "Keep answer clear and structured."
        }
    ]

user_input = st.text_input("Enter mobile name or ask about any phone:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.write("### 📱 Mobile Details")
    st.write(reply)
