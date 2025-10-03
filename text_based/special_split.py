Text = "Remove HTML. Tags from a String?"

import re

def split_sentences_to_lists(text):
    # Remove any unwanted HTML tags (if there are any)
    text = re.sub(r'<.*?>', '', text)
    
    # Use regex to split the text by sentence-ending punctuation marks
    sentences = re.split(r'(?<=\w[.!?])\s+', text)
    
    # Convert each sentence into a list of words
    sentence_lists = [sentence.split() for sentence in sentences]
    
    return sentence_lists

# Test the function

output = split_sentences_to_lists(Text)
print(output)