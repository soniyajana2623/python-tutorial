'''
REGULAR EXPRESSION:
Short form is "regex". Aloow you to match and manipulate strings based on patterns,
making it easy to perform complex string operation with just few lines of code.
'''

'''
[] Represent a character class
+  One or more occarance

'''

import re


pattern="Hello"
# p= r"[A-Z]+ello   (match the starting letter + the rest for the letter)
text='''
Hello my name is Soniya Jana. I am 21 years old.
'''

# match= re.search(pattern,text)    #for single match only(it will show only the 1st match)
# print(match)


m1= re.finditer(pattern,text)     #for every match in the text(it will show all the matches in the text)
for m in m1:
    # print(m)
    print((m.span()))        #tells the index of the match(starting, ending)
    print(text[m.span()[0]:m.span()[1]])        #tells the index of the match(starting, ending)




