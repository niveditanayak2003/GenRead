from models.qa_model import load_qa_model
from models.t5_model import generate_answer_t5

qa_model=load_qa_model()

def get_answer(context,question,mode="Exctractive"):
    if mode=="Extractive":
        result=qa_model(question=question, context=context)
        return result['answer'],result['score']
    elif mode=="Generative":
        answer=generate_answer_t5(context,question)
        return answer,None