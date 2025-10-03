def remove_ascii(text):
    pass

text = 'Café au lait, voilà!'

a = ''.join(i for i in text if ord(i) < 128)
print(a)