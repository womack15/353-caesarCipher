#!/usr/bin/env python2

"""
Joshua Womack
CPSC 353 - Intro to Security
Fall 2016
"""

import sys


def main():
    charCount = 0
    ciphertext = ''
    freqdict = {}
    letterfreq = {97:8.167, 98:1.492, 99:2.782, 100:4.253, 101:12.702, 102:2.228, 103:2.105, 104:6.094, 105:6.966}

    try:
        for i in range(1, len(sys.argv)):
            ciphertext += sys.argv[i]

        ciphertext = ciphertext.lower()

        for i in range(len(ciphertext)):
            if ciphertext[i] != ' ':
                charCount += 1

        for i in range(len(ciphertext)):
            freqdict[ord(ciphertext[i])] = freqdict.get(ord(ciphertext[i]), 0) + 1

        for key, value in freqdict.items():
            freqdict[key] = (float(freqdict[key]) / 35) * 100

        for key, value in freqdict.items():
            print '{}: {}'.format(chr(key), value)

#        for key, value in freqdict.items():
#            freqdict[key] = letterfreq[key]


    except:
        print 'frequency.py unknown arguments'
        print 'Usage:'
        print '\tpython frequency.py <Message>'
        print '\t<Message> --> Plaintext to encrypt'
        exit(-1)


if __name__ == "__main__":
    main()
