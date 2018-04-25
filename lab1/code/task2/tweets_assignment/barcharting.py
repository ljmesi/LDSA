#!/usr/bin/env python3
"""barcharting.py"""

import sys
import matplotlib.pyplot as plt
import numpy as np

han = 0
hon = 0
hen = 0
den = 0
det = 0
denna = 0
denne = 0
count = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    han, hon, hen, den, det, denna, denne, count = line.split('\t')
    try:
        han = int(han)
        hon = int(hon)
        hen = int(hen)
        den = int(den)
        det = int(det)
        denna = int(denna)
        denne = int(denne)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

words = ('han','hon','hen','den','det','denna','denne')
y_pos = np.arange(len(words))
counts = [han/count,hon/count,hen/count,den/count,det/count,denna/count,denne/count]

plt.bar(y_pos, counts, align='center', alpha=0.5)
plt.xticks(y_pos, words)
plt.ylabel('Normalised count')
plt.title('Relative amount of occurences of words')
plt.show()
