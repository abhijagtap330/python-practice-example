import re

text = "I'm learning #Python & #MachineLearning!"

def extract_text(text):
    clean = re.findall(r'\#\w+', text)
    return clean

print(extract_text(text))

def extract_money_values(text):
    return re.findall(r'\b[€$£]\D+(\.\d{2})?\b', text)

print(extract_money_values("The price is $50, and the total is €100.00."))