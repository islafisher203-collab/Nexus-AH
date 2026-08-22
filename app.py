import streamlit as st
from groq import Groq

# Website ka Title aur Page Setup
st.set_page_config(page_title="Nexus-AH Super AI", page_icon="🧠", layout="centered")

st.title("🧠 Nexus-AH")
st.subheader("The Ultimate Super-AI Matrix")
st.write("Ask me anything! I am powered by Llama 3 and customized just for you.")

# Shuru ka hissa maine likh diya hai
part1 = "gsk_"

# APNI NAYI KEY KA 'gsk_' KE BAAD VALA POORA HISSA IS DOUBLE QUOTES KE ANDAR PASTE KAREIN
part2 = "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"

asli_key = part1 + part2
client = Groq(api_key=asli_key)

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
            # Groq Server se jawab mangna
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=False,
                temperature=0.7,
            )
            full_response = completion.choices.message.content
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = "Maaf kijiyega, server se connect karne mein masla aa raha hai."
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
