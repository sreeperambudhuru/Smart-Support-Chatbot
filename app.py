import streamlit as st
import re # This helps us find patterns like numbers

st.set_page_config(page_title="Support Bot", page_icon="🤖")
st.title("🤖 Smart Support Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("How can I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    query = prompt.lower()
    
    # 1. Check for Order ID (Entity Recognition)
    # This looks for any 5-digit number in the text
    order_id = re.search(r'\d{5}', query)
    
    # 2. Support Flows
    if any(word in query for word in ["order", "package", "track"]):
        if order_id:
            response = f"📦 **Tracking Update:** I found Order #{order_id.group()}. It is currently in transit and will arrive in 2 days!"
        else:
            response = "📦 **Order Status:** I can help with that! Please provide your 5-digit Order ID."
            
    elif any(word in query for word in ["refund", "money", "return"]):
        response = "💰 **Refund Info:** Returns are accepted within 30 days. Would you like a return link?"
    
    else:
        response = "🤔 I'm not sure about that. Try asking about 'orders' or 'refunds'!"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)