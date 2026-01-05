import re

def clean_text(text):
    if not text:
        return []   # for empty string the function returns an empty list

    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text) #removes all characters except lowercase letters and spaces
    return text.split()  #returns the token list
