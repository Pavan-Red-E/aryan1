from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from nltk import sent_tokenize

def Captalize(text):
    f=0
    total=0
    for i in text:
        if f==1:
            Cap=i.capitalize()
            if Cap!=i:
                total+=1
        if i=='.':
            f=1
        else:
            f=0
    count=0
    num_tokens=len(text.split())
    vowels=['a','e','i','o','u','A','E','O','U','I']
    for i in range(0,num_tokens):
        if text[i]=='a':
            if text[i+1][0] in vowels:
                count+=1
        if text[i]=='an':
            if text[i+1][0] not in vowels:
                count+=1
    sum=total+count
    return sum