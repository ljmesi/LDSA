#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

han_count = 0
hon_count = 0
hen_count = 0
den_count = 0
det_count = 0
denna_count = 0
denne_count = 0
total_count = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    han, hon, hen, den, det, denna, denne, count = line.split('\t')
    # convert count (currently a string) to int
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
    han_count += han
    hon_count += hon
    hen_count += hen
    den_count += den
    det_count += det
    denna_count += denna
    denne_count += denne
    total_count += count
# write result to STDOUT
print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (han_count,hon_count,hen_count,den_count,det_count,denna_count,denne_count,total_count))