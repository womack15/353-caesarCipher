#!/usr/bin/env python2

import sys


def main():
    ciphertext = ''
    freqdict = {}

    try:
        for i in range(1, len(sys.argv)):
            ciphertext += sys.argv[i]

        ciphertext = ciphertext.lower()

        for i in range(len(ciphertext)):
            freqdict[ord(ciphertext[i])] = freqdict.get(ord(ciphertext[i]), 0) + 1

        for key, value in freqdict.items():
            print '{}: {}'.format(chr(key), value)


    except:
        print 'frequency.py unknown arguments'
        print 'Usage:'
        print '\tpython frequency.py <Message>'
        print '\t<Message> --> Plaintext to encrypt'
        exit(-1)


if __name__ == "__main__":
    main()