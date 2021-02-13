handle = open('mbox-short.txt')
# in len(handle) < 1 : handle = 'mbox-short.txt'
words = list() #lista de values similares a strings
count = dict() #lista de values fora de ordem, similares a inteiros

# Limpeza de blankspaces, Começa em From
for line in handle:
	line = line.rstrip()
	if line.startswith('From ') :
		line = line.split()
		words.append(line[1]) # Lista 1...From: primeira posição, segundo valor ja é o email

# Contador
for word in words:
	count[word]= count.get(word, 0) + 1

# Chaves e valores
bigcount = None
bigword = None
for key,values in count.items():
	if bigcount is None or values > bigcount:
		bigcount = values
		bigword = key
        
print(bigword, bigcount)