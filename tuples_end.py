fhand = open('mbox-short.txt')
counts = dict()

#LIMPEZA E CONTAGEM DE PALAVRAS
for line in fhand:
    word = line.split()
    for words in word:
        counts[words] = counts.get(words, 0) + 1

# Lista de Tuples em ordem value-key 
lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)

# lst = sorted(lst, reverse=True) # Maior para o menor valor

for value, key in lst[:10]:
    print(key, value)

# Alternative way
# c = {'a':10, 'b':1, 'c':22}
# print(sorted( [ (v,k) for k,v in c.items() ] ) ) 