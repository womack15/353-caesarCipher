#!/usr/bin/env python2

"""
Joshua Womack
CPSC 353 - Intro to Security
Fall 2016
"""

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
            print message

        elif mode == "-d":
            message = sys.argv[2]
            print 'Decrypting...'
            message = decrypt(message)
            print 'All possible plaintext:'

            for text in message:
                print text

            print

        else:
            raise Exception


    except:
        print 'caesar.py unknown arguments'
        print 'Usage: python caesar.py <-e|-d> <N> <Message>'
        print '  <-e>\t\tencrypt'
        print '  <-d>\t\tdecrypt'
        print '  <N>\t\tPositive ingeger specifying how much to rotate by'
        print '  <Message>\tPlaintext to encrypt\n'
        exit(-1)


def encrypt(rot, plaintext):
    message = ""
    for char in plaintext:
        if 0x40 < ord(char) < 0x5b:
            # Uppercase
            newval = ord(char) + rot
            if newval > 0x5a:
                newval = newval - 26
            char = chr(newval)

        elif 0x60 < ord(char) < 0x7b:
            # Lowercase
            newval = ord(char) + rot
            if newval > 0x7a:
                newval = newval - 26
            char = chr(newval)

        message = message + char

    return message


def decrypt(ciphertext):
    tempList = []
    for i in range(1, 27):
        tempList.append(encrypt(i, ciphertext))
    return tempList

if __name__ == "__main__":
    main()
