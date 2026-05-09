import streamlit as st
from bot import get_answer
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style.css")

# Page setup
st.set_page_config(
    page_title="Medical FAQ Bot",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("🩺 Medical FAQ Bot")
st.sidebar.markdown("Navigate through categories:")
st.sidebar.button("Symptoms")
st.sidebar.button("Treatments")
st.sidebar.button("First Aid")
st.sidebar.info("💡 Try asking: *What are the symptoms of diabetes?*")

# Gradient header
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: -webkit-linear-gradient(#2E86C1, #58D68D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    <h1 class="main-title">Medical FAQ Assistant 💊</h1>
    """,
    unsafe_allow_html=True
)

# Input + Answer card
user_question = st.text_input(
    "Ask your medical question:",
    placeholder="e.g. What are the symptoms of malaria?"
)

if user_question:
    answer = get_answer(user_question)
    st.markdown(
        f"""
        <div style="background-color:#F4F6F7;
                    padding:20px;
                    border-radius:12px;
                    margin-top:20px;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <b>Answer:</b> {answer}
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:grey;">
    ⚕️ Powered by Streamlit | Designed for Medical FAQs
    </p>
    """,
    unsafe_allow_html=True
)
