VOWELS = 'aeiou'

def contador(sentence):
    result = 0
    for x in sentence:
        if x in VOWELS:
            result+=1
    return result

def contador2(sentence):
    result = []
    for x in sentence:
        if x in VOWELS:
            result.append(x)
    return len(result)

sentence = 'we are studying list comprehensions'
print(contador(sentence))
print(contador2(sentence))

lista = [600, 1, 2, -1]

def max_(datos):
    result = None
    for x in datos:
        if result == None or result<x:
            result = x
    return result

def min_(datos):
    result = None
    for x in datos:
        if result == None or result>x:
            result = x
    return result

print(max(lista), max_(lista), min(lista), min_(lista))
