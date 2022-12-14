# -*- coding: utf-8 -*-
"""Token generate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QXj3ZGg_QcK4MyZ-BEa0jpTpPZddYfP3
"""

import re
import nltk
from collections import OrderedDict

key = []
key_count = 0
ope = []
ope_count = 0
con = []
con_count = 0
iden = []
iden_count = 0
par = []
par_count = 0
pun = []
pun_count = 0

string = input("Enter a Code String: ")

token = nltk.wordpunct_tokenize(string)
token

token = list(OrderedDict.fromkeys(token))
token

try:
   index = token.index('#') 
   token = token[0:index]
except:
   pass

print(token)
print(' '.join(token))

punctuation = "(,)|(;)|(:)"
keyword = "if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield|False|None|True|and|as|assert|async|await|break|continue|def|del|elif|else|expect|finally|for|from|global"
operator = "(\++)|(-)|(=)|(\*)|(%)|(--)|(<=)|(>=)|(/)|(&)|(!)"
constant = "^(\d+)$"
identifier = "^[a-z|A-Z|_]+[a-z|A-Z|0-9|_]*"

for i in token:
    if re.findall(keyword, i):
        key.append(i)
        key_count = key_count + 1
    elif re.findall(operator, i):
        ope.append(i)
        ope_count = ope_count + 1
    elif re.findall(constant, i):
        con.append(i)
        con_count = con_count + 1
    elif re.findall(identifier, i):
        iden.append(i)
        iden_count = iden_count + 1
    elif re.findall(punctuation, i):
        pun.append(i)
        pun_count = pun_count + 1
    else:
        par.append(i)
        par_count = par_count + 1


print("Keyword = ", key, " & Total no of Keyword = ", key_count)
print("Operator = ", ope, " & Total no of Operator = ", ope_count)
print("Constant = ", con, " & Total no of Constant = ", con_count)
print("Identifier = ", iden, " & Total no of Identifier = ", iden_count)
print("Punctuation = ", pun, " & Total no of Punctuation = ", pun_count)
print("Parentheses = ", par, " & Total no of Parentheses= ", par_count)