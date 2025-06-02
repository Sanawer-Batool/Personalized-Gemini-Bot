import streamlit as st
import google.generativeai as genai

# Set your Gemini API key
GEMINI_API_KEY = "API-KEY"  # Replace with your actual key
genai.configure(api_key=GEMINI_API_KEY)

# Function to interact with Gemini API with error handling
def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error communicating with Gemini API: {str(e)}")
        return "Sorry, I couldn't process your request."

# Custom CSS for a professional and appealing design
st.markdown("""
    <style>
    .main {
        background: linear-gradient(rgba(10, 10, 35, 0.9), rgba(10, 10, 35, 0.9)), 
                   url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-position: center;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: rgba(26, 26, 61, 0.9);
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    .stTitle {
        text-align: center;
        color: #00d4ff;
        text-shadow: 0 0 10px #00d4ff, 0 0 20px #ff00ff;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #1a1a3d;
        color: #00d4ff;
        border: 2px solid #ff00ff;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #00d4ff;
        color: #0a0a23;
        border-radius: 15px;
        font-weight: bold;
        padding: 12px 24px;
        border: 2px solid #ff00ff;
        box-shadow: 0 0 10px #00d4ff;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #ff00ff;
        color: #ffffff;
        box-shadow: 0 0 15px #ff00ff;
    }
    .chat-message {
        padding: 10px 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.1);
        animation: fadeIn 0.5s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .user-message {
        background-color: #1a1a3d;
        text-align: right;
    }
    .bot-message {
        background-color: #0a0a23;
        text-align: left;
    }
    .sidebar .sidebar-content {
        background-color: rgba(26, 26, 61, 0.9);
        color: #00d4ff;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app layout
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("Gemini AI ChatBot 🤖")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar with Quick Tips
with st.sidebar:
    st.markdown("### 🚀 About This ChatBot")
    st.markdown("Welcome to the Gemini AI ChatBot! Powered by Google's generative AI, this app provides intelligent responses to your questions. 🌌")
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.markdown("- Ask open-ended questions for detailed answers.")
    st.markdown("- Try topics like science, history, or coding.")
    st.markdown("- Use 'explain' or 'summarize' for better results.")

# Use a form for input and submission
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask me anything:", key="user_input")
    submit_button = st.form_submit_button(label="Send")

# Process the input when the form is submitted
if submit_button and user_input:
    response = chat_with_gemini(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "bot", "content": response})

# Display the chat history
if st.session_state.chat_history:
    for message in st.session_state.chat_history:
        message_class = "user-message" if message["role"] == "user" else "bot-message"
        st.markdown(f'<div class="chat-message {message_class}"><strong>{message["role"].capitalize()}:</strong> {message["content"]}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="chat-message bot-message"><strong>Bot:</strong> Hello! Ask me anything to start the conversation.</div>', unsafe_allow_html=True)

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []

st.markdown('</div>', unsafe_allow_html=True)
