import streamlit as st
import requests

st.set_page_config(page_title="Nexus-AH Super AI", page_icon="🧠", layout="centered")

st.title("🧠 Nexus-AH")
st.subheader("The Ultimate Super-AI Matrix")
st.write("Ask me anything! I am powered by Open-Source AI and customized just for you.")

# Hugging Face Public Model (No Keys, No Secrets, No Bots blocking)
API_URL = "https://huggingface.co"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Nexus-AH se baat karein..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            payload = {"inputs": prompt, "parameters": {"max_new_tokens": 250}}
            response = requests.post(API_URL, json=payload)
            output = response.json()
            
            if isinstance(output, list) and "generated_text" in output:
                full_response = output["generated_text"]
                if prompt in full_response:
                    full_response = full_response.replace(prompt, "").strip()
            else:
                full_response = "Nexus-AH ready ho raha hai, 5 seconds baad dobara try karein."
                
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = "Network connect karne mein masla aa raha hai."
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
