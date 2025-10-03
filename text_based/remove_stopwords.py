input = "This is a simple example of text cleaning."
stop_words = ['This', 'is', 'a', 'of']

def remove_stopwords(text):
    words = text.split()
    return ' '.join([word for word in words if word.lower() not in stop_words])

print(remove_stopwords(input))

import re
def tokenized(text):
    a = re.sub(r'[^A-Za-z]', ' ', text)
    words = str(a.split())
    return words

print(tokenized(input))