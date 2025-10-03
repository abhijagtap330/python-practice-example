text = "This is\n     a  test\tstring"

import re
def remove_white_space(text):
    text = re.sub(r'\s+', ' ', text)
    return text
    
print(remove_white_space(text))
    
    
def extract_invoice(text):
    return re.findall(r'INV-\d{5}', text)

print(extract_invoice("The invoice numbers are INV-12345 and INV-67890."))