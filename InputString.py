import sys
from itertools import permutations
from spellchecker import SpellChecker

spell = SpellChecker(language='de')

inputstr = "pearlhn".upper()
print (inputstr)

perms = (p for p in permutations(inputstr.upper()))
for p in perms:
    localstring = ''
    newstring  = (localstring.join(p))
    newstring = newstring.lower()
    if newstring in spell:
        print("'{}' is spelled correctly!".format(newstring))
    
    

