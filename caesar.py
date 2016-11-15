#!/usr/bin/env python2

import sys


def main():
    try:
        mode = sys.argv[1].lower()

        # Encrypt or decrypt?
        if mode == "-e":
            if (not sys.argv[2]) or sys.argv[2] < 0:
                raise Exception
            else:
                rot = int(sys.argv[2])
                message = sys.argv[3]
            print 'Encrypting...'
            message = encrypt(rot, message)

        elif mode == "-d":
            message = sys.argv[2]
            print 'Decrypting...'
            message = decrypt(message)
        else:
            raise Exception

        print message

    except:
        print 'caesar.py unknown arguments'
        print 'Usage:'
        print '\tpython caesar.py <-e|-d> <N> <Message>'
        print '\t-e --> encrypt'
        print '\t-d --> decrypt'
        print '\t N --> Positive ingeger specifying how much to rotate by'
        print '\tMessage --> Plaintext to encrypt'
        exit(-1)


def encrypt(rot, plaintext):
    message = ""
    for char in plaintext:
        if ord(char) > 0x41 and ord(char) < 0x5a:
            # Uppercase
            newval = ord(char) + rot
            if newval > 0x5a:
                newval = newval - 26
            char = chr(newval)

        elif ord(char) > 0x61 and ord(char) < 0x7a:
            # Lowercase
            newval = ord(char) + rot
            if newval > 0x7a:
                newval = newval - 26
            char = chr(newval)

        message = message + char

    return message


def decrypt(ciphertext):
    for i in range(1, 26):
        print encrypt(i, ciphertext)
    return None

if __name__ == "__main__":
    main()
