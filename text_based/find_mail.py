Input = "Hello, World! This is a test. abhijeetjagtap330@gmail.com"

import re
def extract_mail(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(email_regex, text)
    
print(extract_mail(Input))