#!/opt/homebrew/bin/python3
# 111211

from re import *

xina = "1xinamEn2345"
print(search("xin..[c-j,A-Z]n",xina))
print(search("[^a-z]","1abcdjkd"))
print(search(r"\W",xina))
print(search(r"",xina))