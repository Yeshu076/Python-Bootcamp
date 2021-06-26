# Write a Python program for all the cases which can check a string contains only a certain set of characters

import re
def a_1(stiing):
    charRE = re.compile(r'[^a-zA-Z0-9.]')
    stiing = charRE.search(stiing)
    return not bool(stiing)
print(a_1("5./%^%$**^;"))
print(a_1("skjdsfhskfhfkhkzbjdgejfakhai33543443545"))

#_________________________________________x_______________________________________________
#Write a Python program that matches a word containing 'ab'

import re
def w_1(aqwe):
    patterns = '\w\d'
    if re.search (patterns, aqwe):
        return 'found a match!'
    else:
        return ('Not matched!')

print(w_1("the quick brown fox jumps over the lazy"))
print(w_1('rishab'))

#------------------------------------------x----------------------------------------------
#Write a Python program to check for a number at the end of a word/sentence.

import re
def w_7(text):
    pattern = re.compile(r'.*[0-9]$')
    if pattern.match(text):
        return 'found match!'
    else:
        return ('Not matched!')

print(w_7("vdhgfhfgdhj9"))
print(w_7('hhghgkjgjfkhkr'))

#--------------------------------------------x-------------------------------------------
#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
results = re.finditer(r'([0-9]{1,3})', 'Exercises number 1,12,13, and 345 are important')
print('number of length 1 to 3')
for n in results:
    print(n.group(0))

#---------------------------------------------x------------------------------------------
#Write a Python program to match a string that contains only uppercase letters

import re
def w_9(sddd):
    pat = '[^A-B.]'
    if re.search (pat, sddd):
        return 'found a match!'
    else:
        return ('Not matched!')

print(w_9("SJHFKSFHKSFSHF"))
print(w_9("GHJGJGJ"))