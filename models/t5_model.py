from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer=AutoTokenizer.from_pretrained("t5-base")
model=AutoModelForSeq2SeqLM.from_pretrained("t5-base")

def generate_answer_t5(context,question):
    input_text=f"question:{question} context: {context}"
    inputs=tokenizer.encode(input_text,return_tensors="pt",max_length=512,truncation=True)
    outputs=model.generate(inputs,max_length=100,early_stopping=True)
    answer=tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer