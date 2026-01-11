#import streamlit as st
#from dotenv import load_dotenv

#load_dotenv()

#import google.generativeai as genai
#import os

#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
import os
import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# -----------------------
# Setup
# -----------------------
load_dotenv()
st.set_page_config(page_title="UI-Constrained Agent", layout="centered")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

MAX_CHARS = 120

# -----------------------
# Session State
# -----------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "product" not in st.session_state:
    st.session_state.product = ""

if "audience" not in st.session_state:
    st.session_state.audience = ""

if "result" not in st.session_state:
    st.session_state.result = ""

if "confidence" not in st.session_state:
    st.session_state.confidence = 0.0

# -----------------------
# Helper Functions
# -----------------------
def constrained_generate(prompt: str):
    response = llm.invoke(prompt).content.strip()
    return response[:MAX_CHARS]

def show_status(label, done):
    st.write(f"{'✅' if done else '⏳'} {label}")

# -----------------------
# UI
# -----------------------
st.title("🧠 UI-Constrained Agent")

st.subheader("Task: Create a product description")

show_status("Product name provided", st.session_state.step > 1)
show_status("Target audience provided", st.session_state.step > 2)
show_status("Description generated", st.session_state.step > 3)

st.divider()

# -----------------------
# Step 1 – Product Name
# -----------------------
if st.session_state.step == 1:
    product = st.text_input("Enter product name", value=st.session_state.product)

    if st.button("Confirm product"):
        st.session_state.product = product
        st.session_state.step = 2

# -----------------------
# Step 2 – Audience
# -----------------------
elif st.session_state.step == 2:
    audience = st.text_input(
        "Enter target audience",
        value=st.session_state.audience,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Confirm audience"):
            st.session_state.audience = audience
            st.session_state.step = 3

    with col2:
        if st.button("Edit product"):
            st.session_state.step = 1

# -----------------------
# Step 3 – Generate
# -----------------------
elif st.session_state.step == 3:
    prompt = PromptTemplate(
        template=(
            "Write a short product description for {product} "
            "aimed at {audience}. Keep it concise and clear."
        ),
        input_variables=["product", "audience"],
    )

    if st.button("Generate description"):
        text = constrained_generate(
            prompt.format(
                product=st.session_state.product,
                audience=st.session_state.audience,
            )
        )

        st.session_state.result = text
        st.session_state.confidence = 0.85  # simulated confidence score
        st.session_state.step = 4

# -----------------------
# Step 4 – Review & Correct
# -----------------------
elif st.session_state.step == 4:
    st.subheader("Agent Output")

    st.success(st.session_state.result)

    st.metric(
        label="Agent confidence",
        value=f"{int(st.session_state.confidence * 100)}%",
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Accept"):
            st.balloons()

    with col2:
        if st.button("Edit audience"):
            st.session_state.step = 2

    with col3:
        if st.button("Regenerate"):
            st.session_state.step = 3
