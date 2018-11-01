# Different algorithms to reverse words of a sentence.
This repo contains some fun algorithms to reverse words of a sentence. This is a popular interview question - so this repo will show few different ways to solve it.

## Problem
Reverse words of a sentence. For example, if you are given input *'you shall not pass'*, it should return *'pass not shall you'*.

As a bonus challenge, the program should take care of punctuations. (Punctuations should appear in the same order as in the original sentence). For example - *'you, shall not pass!'* should result in *'pass, shall not you!'*

You can submit pull requests for solutions for any other language - and I will promise to get it merged for you :-)


## Python
Python provides many ways to manipulate strings - and this repo contains a few examples of how powerful Python's regex and string management library is.

### Split the sentence, reverse it and join it back
Let's start with simple method first. Python provides split() method - with which we can break the words of a string. Then all we have to do is reverse this list and join them.

```
simple-reverse-words.py
s = 'you shall not pass'
r = ' '.join(reversed(s.split(' ')))
```

How it works:
- `s.split(' ')` splits the strings using space as a separating character. It returns an array of words that have been split.
- `reversed(list)` returns the reversed string.
- `'separator'.join(words)` joins the words using the separator. In this case, we are joining them by space character.

What it lacks:
- This does not take care of any punctuations.
- *'you shall not pass!'* would be converted to *'pass! not shall you'*  (ugh)


### Use Python's regex modules
Another simple way in Python is to split using regex module. This will allow us to split based on space as well as punctuations.

In this case we want to find all words and punctuations - and collect them as different items in an array. Then we need to just reverse the words, while keeping those punctuations in the same place.

```
>>> import re
>>> re.findall('[:;,.!?]', 'you, shall not pass!!')
[',', '!', '!']

```

Cool - this is a good start. This regex `[:;,.!?]` is allowing us to isolate all punctuations from the string. Now the next step is to isoloate it in conjunctions with the words in the sentence. Before that, I wanted to give a quick overview of what just happened here in terms of regex.
- I am using this set `{',', '.', '!', ':', ';', '?'}` as the set of all punctuations - you can feel free to add more punctuations here if needed.
- We are using `findall` method of `re` - which allows to find *all* matches of a given regex.
- Square bracket `[]` is needed a single character match with an OR condition. For ex., `[:;,.!?]` is same as `:|;|,|.|!|?`

The above snippet does not include actual words of the list. This should be easy to fix.

```
>>> import re
>>> re.findall('\w+|[:;,.!?]', 'you, shall not pass!!')
['you', ',', 'shall', 'not', 'pass', '!', '!']
```

Awesome - now we need to reverse any words which are not a punctuation and we will have our final program. In order to do the reversal - we will use two pointers: one going left-to-right and another going right-to-left. We swap what these pointers are pointing to when *both* pointers are not pointing to a punctuation.

This is the final program.
```
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
```

### Third method (Regex)
I hate the ugliness of the regex method provided above. When I started writing it, I felt it should not be more than 3-4 lines but it turned out to be too gnarly.

I feel the complexity is coming from the fact that punctuations need to maintain their word-wise positions. I am not sure if this assumption is likely in many interviews - so I will try to provide another quick-solution to a slightly modified problem.

Say we modify the problem statement for punctuations as: *punctuations need to be associated with their original word, except the end ones which should always remain at the end*. For ex., *'you shall, not pass!!'* should convert to *'pass not shall, you!!'*

In my opinion, this would likely produce better gibberish sentences than the second method :-)

With this definition - we can consider all punctuations to be part of the word they are after - simplifying our split and reverse logic. We still need to treat punctuations at the end of line separately - but that would be just an additional line of code.

Here is the complete code.

```
import re

punctuations = ':;,.!?'
inp = 'you shall not, pass!!'
match = re.search(r'([:;,.!?]+)$', inp)
end_puncs = match.group(1) if match is not None else ''
rev = ' '.join(reversed(re.findall('[\w:;,.!?]+', inp.rstrip(punctuations)))) + end_puncs
print(rev)
```

OK, that was like three lines of code! Let's walk through it to see what it does.
- `punctuations` is an array of all punctuations.
- First we try to search any punctuations at the end of the line, so we can add it back to the results string.
- The `$` symbol in regex is to specify that the search is for the end of line. We use this this regex to search for all punctuations at the end of line and store them in a string variable.
- The next line is similar to method-1 above - we strip the last punctuations, then split rest of the words. We then reverse that array and join it back to make a string.
- Finally we add back the end punctuations we stored earlier (`end_puncs`)

