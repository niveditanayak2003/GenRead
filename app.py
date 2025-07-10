import streamlit as st
from app.utils import get_answer
from explain.explain import show_attention

#page configuration
st.set_page_config(
    page_title="GenRead- AI Question Answering",
    layout="centered",
    page_icon="🧠"
)

#Load the custom CSS
with open("app/styles.css")as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

#Title and description
st.markdown("<h1>🧠GenRead</h1>",unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>Ask questions from any paragraph. Get AI-powered answers and visual explanations.</p>",
    unsafe_allow_html=True
)
# --- Input Section ---
context = st.text_area("📚 Enter your context/paragraph", height=200)
question = st.text_input("❓ Ask a question")

mode = st.selectbox("Select Answer Mode", ["Extractive (BERT)", "Generative (T5)"])
selected_mode = "Extractive" if "Extractive" in mode else "Generative"

# --- Answer Generation ---
if st.button("🔍 Get Answer"):
    if context.strip() and question.strip():
        with st.spinner("Thinking..."):
            answer, score = get_answer(context, question, mode=selected_mode)

        if score is not None:
            st.success(f"💬 Answer: {answer}\n\nConfidence: {score:.2f}")
        else:
            st.success(f"💬 Generated Answer: {answer}")

        if selected_mode == "Extractive":
            with st.spinner("🎯 Generating attention heatmap..."):
                show_attention(context, question)
                st.image("attention_heatmap.png", caption="Attention Heatmap (BERT)", use_column_width=True)
    else:
        st.warning("⚠️ Please enter both context and question to continue.")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center; font-size: 14px;'>Built with ❤️ by Nivedita using HuggingFace + Streamlit</p>", unsafe_allow_html=True)
