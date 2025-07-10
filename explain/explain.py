import matplotlib.pyplot as plt
import torch
from transformers import AutoTokenizer,AutoModelForQuestionAnswering

def show_attention(context,question):
    tokenizer=AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
    model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad", output_attentions=True)

    inputs=tokenizer(question, context, return_tensors='pt')
    outputs=model(**inputs)

    attentions=outputs.attentions[-1].detach().numpy()
    tokens=tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    plt.figure(figsize=(12,5))
    plt.imshow(attentions[0][0],cmap='viridis')
    plt.title("Attention Heatmap(Last Layer)")
    plt.xlabel("Tokens")
    plt.ylabel("Tokens")

    plt.xticks(range(len(tokens)),tokens,rotation=90)
    plt.yticks(range(len(tokens)),tokens)
    plt.tight_layout()
    plt.savefig("attention_heatmap.png")