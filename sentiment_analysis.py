# sentiment_analysis.py

import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from peft import PeftModel
from preprocess import clean_text

BASE_MODEL_NAME = "distilbert-base-uncased"
ADAPTER_PATH = r""

tokenizer = DistilBertTokenizer.from_pretrained(BASE_MODEL_NAME)
base_model = DistilBertForSequenceClassification.from_pretrained(BASE_MODEL_NAME)
model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_sentiment(text):
    text = clean_text(text)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    sentiment = torch.argmax(probs, dim=1).item()  # 0 for negative, 1 for positive
    confidence = probs[0][sentiment].item()
    return sentiment, confidence


