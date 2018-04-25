#!/usr/bin/env python3
"""plot_freq.py"""

import sys
import matplotlib.pyplot as plt
import numpy as np

characterlist = []
frequencylist = []
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    character, frequency = line.split('\t')
    characterlist.append(character)
    try:
        frequency = int(frequency)
        frequencylist.append(frequency)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

alphabet = characterlist[23:49]
alphabet_frequency = frequencylist[23:49]
y_pos = np.arange(len(alphabet))

plt.bar(y_pos, alphabet_frequency, align='center', alpha=0.5)
plt.xticks(y_pos, alphabet)
plt.ylabel('Alphabet count')
plt.title('A count of each alphabet')
plt.show()
