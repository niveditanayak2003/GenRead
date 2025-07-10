from transformers import pipeline

def load_qa_model():
    #Loads a predefined BERT QA model
    qa_pipeline=pipeline("question-answering",model="distilbert-base-cased-distilled-squad")
    return qa_pipeline
