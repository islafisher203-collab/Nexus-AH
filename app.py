import streamlit as st
import requests

# Website ka Title aur Page Setup
st.set_page_config(page_title="Nexus-AH Super AI", page_icon="🧠", layout="centered")

st.title("🧠 Nexus-AH")
st.subheader("The Ultimate Super-AI Matrix")
st.write("Ask me anything! I am powered by Open-Source AI and customized just for you.")

# Hugging Face Public API Connection (No Private Keys Needed)
API_URL = "https://huggingface.co"

# Chat history ka system (Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ka naya message lena
if prompt := st.chat_input("Nexus-AH se baat karein..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI ka jawab tayyar karna
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Hugging Face Public Server se jawab mangna
            payload = {"inputs": prompt, "parameters": {"max_new_tokens": 250}}
            response = requests.post(API_URL, json=payload)
            output = response.json()
            
            if isinstance(output, list) and "generated_text" in output[0]:
                full_response = output[0]["generated_text"]
                # Sirf naya jawab nikalne ke liye prompt ko mita dena agar sath aaye
                if prompt in full_response:
                    full_response = full_response.replace(prompt, "").strip()
            else:
                full_response = "Nexus-AH ready ho raha hai, meherbani kar ke 5 seconds baad dobara bhejiyega."
                
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = "Maaf kijiyega, network connect karne mein masla aa raha hai."
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
