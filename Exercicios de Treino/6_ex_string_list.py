rword = input('Enter a word:')
rword = str(rword)

rev = rword[::-1]
print(rev)

if rword == rev:
    print('It is a palindrome')
else:
    print('Not a palindrome')
