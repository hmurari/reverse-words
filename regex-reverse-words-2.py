import re

punctuations = ':;,.!?'
inp = 'you shall not, pass!!'
match = re.search(r'([:;,.!?]+)$', inp)
end_puncs = match.group(1) if match is not None else ''
rev = ' '.join(reversed(re.findall('[\w:;,.!?]+', inp.rstrip(punctuations)))) + end_puncs
print(rev)
