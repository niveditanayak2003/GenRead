# 🧠 GenRead – Context-Aware AI Reader with Explainable Answers

[![Python](https://img.shields.io/badge/Built%20with-Python-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-ff4b4b?logo=streamlit)](https://streamlit.io/)
[![HuggingFace](https://img.shields.io/badge/Powered%20by-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

> **GenRead** is an AI-powered Question Answering app that not only gives accurate responses from a given passage using **BERT** and **T5**, but also shows *why* it picked that answer using attention heatmaps (for extractive mode).

---

## 🚀 Features

- 🔎 Ask questions from any custom paragraph
- 🤖 Choose between **Extractive (BERT)** or **Generative (T5)** answering
- 🎯 Visual explanation of answers using **attention heatmaps**
- 🌈 Clean UI with a beautiful pastel theme
- ⚡ Easy to run locally or deploy on Streamlit Cloud

---

## 🛠️ Tech Stack

- Python 3.10+
- HuggingFace Transformers (`bert-base-uncased`, `t5-small`)
- Streamlit (Frontend UI)
- Matplotlib (for attention visualizations)
- Custom CSS for beautiful theming

---

```
GenRead/
├── app.py                  # Main Streamlit app
├── app/
│   ├── utils.py
│   └── styles.css
├── models/
│   ├── qa_model.py         # BERT extractive pipeline
│   └── t5_model.py         # T5 generative model
├── explain/
│   └── explain.py          # Attention heatmap visualizer
├── requirements.txt
└── README.md
```


---

## 📦 Installation & Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/genread.git
cd genread

# Create and activate virtual environment
python -m venv genread_env
genread_env\Scripts\activate        # For Windows
# or
source genread_env/bin/activate       # For Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 💡 How to Use

1. Paste any paragraph or context 📚  
2. Type your natural language question ❓  
3. Select **Extractive (BERT)** or **Generative (T5)**  
4. Click **Get Answer** 🔍  
5. View the answer + heatmap (if extractive mode is selected)

---
## Live demo
🧠[GenRead](https://genread-qeancs5gbhlvx4wctemscn.streamlit.app/)
---
---

## 👤 Author

**Nivedita**  
🎓Compuster Science Graduate | Aspiring ML Engineer | Passionate about Explainable AI  
📫 [LinkedIn](https://www.linkedin.com/in/nivedita33)

---
## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
