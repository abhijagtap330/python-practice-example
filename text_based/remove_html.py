text = "<p>Hello <b>World</b></p>"

import re

def remove_html(text):
    return re.sub(r'<.*?>', '', text)

print(remove_html(text))
    