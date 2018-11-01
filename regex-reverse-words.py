import re

punctuations = ':;,.!?'
inp = 'you, shall not pass!!'
words = re.findall('\w+|[:;,.!?]', inp)

# Use two moving pointers to do the reversal
last = len(words) - 1
first = 0
while (first <= last):

    # Skip punctuations
    while (words[first] in punctuations):
        first += 1
    while (words[last] in punctuations):
        last -= 1

    # Swap
    tmp = words[first]
    words[first] = words[last]
    words[last] = tmp

    # Move the pointers
    first += 1
    last -= 1

# Convert the array back to string.
rev = ''
for word in words:
    if word in punctuations or rev is '':
        rev += word
    else:
        rev += ' ' + word

print(rev)