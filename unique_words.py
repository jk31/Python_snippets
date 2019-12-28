# Script to check how often words are repeated in a text
# I use it for my job applications

import re
from collections import Counter

text = """some text""".lower()

words = re.findall(r'\w+', text)
words = [x for x in words if words.count(x) > 1]
x = Counter(words)

print(x)
