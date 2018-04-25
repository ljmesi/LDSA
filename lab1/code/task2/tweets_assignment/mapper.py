#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
import re

# Compiling regular expressions
search_term1 = re.compile('han', re.IGNORECASE)
search_term2 = re.compile('hon', re.IGNORECASE)
search_term3 = re.compile('hen', re.IGNORECASE)
search_term4 = re.compile('den', re.IGNORECASE)
search_term5 = re.compile('det', re.IGNORECASE)
search_term6 = re.compile('denna', re.IGNORECASE)
search_term7 = re.compile('denne', re.IGNORECASE)
# Setting match hits as 'not match in the beginning'
han = '0'
hon = '0'
hen = '0'
den = '0'
det = '0'
denna = '0'
denne = '0'
count ='0'
# input comes from STDIN (standard input)
for line in sys.stdin:
    # Handling empty lines
    if line.strip():
        try:
            # Reading the tweets
            tweet = json.loads(line)
            # Checking if the tweet is retweeted
            if(tweet['retweeted']==False): # If not checking the matches
                current = tweet['text']
                if search_term1.search(current) is not None:
                    han = '1'
                if search_term2.search(current) is not None:
                    hon = '1'
                if search_term3.search(current) is not None:
                    hen = '1'
                if search_term4.search(current) is not None:
                    den = '1'
                if search_term5.search(current) is not None:
                    det = '1'
                if search_term6.search(current) is not None:
                    denna = '1'
                if search_term7.search(current) is not None:
                    denne = '1'
                count ='1'  
        except:
            continue
    # Printing in the STDOUT the results; the last one just marks a tweet
    print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (han,hon,hen,den,det,denna,denne,count))
    # Resetting values
    han = '0'
    hon = '0'
    hen = '0'
    den = '0'
    det = '0'
    denna = '0'
    denne = '0'
    count ='0'
