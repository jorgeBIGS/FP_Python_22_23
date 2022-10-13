VOWELS = 'aeiou'

def consonants_lc(sentence):    
    return [x for x in sentence if x not in VOWELS]

sentence = 'we are studying list comprehensions'
print("With List Comprehension   : " + ''.join(consonants_lc(sentence)))