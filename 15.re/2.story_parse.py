import re
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt


with open('2430AD.txt') as f:
    number_pattern = re.compile(r'\d+\.?\d*')
    a_pattern = re.compile(r'\b\w*[Aa]\w*\b')
    exclamatory_pattern = re.compile(r'\b[A-Z][\w ,\']*!')
    unique_pattern = re.compile(r'\b\w+\b')
    number_matches = []
    a_matches = []
    exclamatory_matches = []
    unique_lengths = Counter()
    for line in f:
        numbers = re.findall(number_pattern, line)
        a = re.findall(a_pattern, line)
        exclamatory = re.findall(exclamatory_pattern, line)
        unique_words = re.findall(unique_pattern, line)
        if numbers:
            number_matches.extend(numbers)
        if a:
            a_matches.extend(a)
        if exclamatory:
            exclamatory_matches.extend(exclamatory)
        for word in unique_words:
            unique_lengths[len(word)] += 1

print(f'Numbers in text: {", ".join(number_matches)}')
print(f'Words with "A" or "a": {", ".join(a_matches)}')
print(f'Exclamatory sentences: {exclamatory_matches}')
sns.barplot(x=list(unique_lengths.keys()), y=list(unique_lengths.values()))
plt.show()
