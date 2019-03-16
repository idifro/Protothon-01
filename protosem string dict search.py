import string
import nltk
from itertools import permutations 
from nltk.corpus import words


if __name__=='__main__':
    
    str = "ProtoSem"
    
    permuList = permutations(str)
        
    for perm in list(permuList): 
        a = ''.join(perm)
        a = a.lower()
        if(a in words.words()):
            print(a)