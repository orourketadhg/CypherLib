import random

"""
Author: Tadhg O'Rourke
Date: 20/12/2018

Project Description:
    A library of cyphers including:
        Caesar Cypher
        Vigenere Cypher
        2X2 Hill Cypher
"""


def _cypher_alphabet():
    return list('abcdefghijklmnopqrstuvwxyz')


def caesar_cypher_encrypt(plaintext, offset):
    alphabet = _cypher_alphabet()
    plaintext_split = list(plaintext.lower())
    unknown_char = []
    encrypted_message = []

    # loop through letters in plaintext
    for letter in plaintext_split:

        # if letter is a space
        if letter == " ":
            encrypted_message.append(" ")

        # elif letter is not in known alphabet
        elif letter not in alphabet:
            continue

        # if letter is known
        elif letter in alphabet:
            letter_value = alphabet.index(letter)
            encrypted_value = (letter_value + offset) % 26
            encrypted_message.append(alphabet[encrypted_value].upper())

    return ''.join(encrypted_message)


def caesar_cypher_decrypt(cyphertext, offset):
    alphabet = _cypher_alphabet()
    cyphertext_split = list(cyphertext.lower())
    decrypted_message = []

    # loop through cyphertext
    for letter in cyphertext_split:

        # if letter is a space
        if letter == " ":
            decrypted_message.append(" ")

        # decrypt letter to get value
        else:
            letter_value = alphabet.index(letter)
            decrypted_value = (letter_value - offset) % 26
            decrypted_message.append(alphabet[decrypted_value].upper())

    return ''.join(decrypted_message)


def vigenere_cypher_encrypt(plaintext, key, space=0):
    alphabet = _cypher_alphabet()
    plaintext = list(plaintext.lower())
    key = list(key)
    encrypted_message = []
    key_count = 0

    # loop through plaintext
    for letter in plaintext:

        #  if key_count at length of key reset to zero
        if key_count == len(key):
            key_count = 0

        # if letter is a space and in space mode - append a space
        if letter == ' ' and space == 1:
            encrypted_message.append(" ")

        # elif non alphabetical char - continue
        elif letter not in alphabet:
            continue

        # else alphabetical char - calculate value, append alphabet letter matching value
        else:
            encrypted_value = (alphabet.index(letter) + alphabet.index(key[key_count])) % 26
            encrypted_message.append(alphabet[encrypted_value].upper())

        # increment key_count
        key_count += 1

    return "".join(encrypted_message)


def vigenere_cypher_decrypt(cyphertext, key, space=0):
    alphabet = _cypher_alphabet()
    cyphertext = list(cyphertext.lower())
    key = list(key)
    decrypted_message = []
    key_count = 0

    # loop through cyphertext
    for letter in cyphertext:

        # if key_count at max length - set to zero
        if key_count == len(key):
            key_count = 0

        # if letter is a space and space mode enabled - append a space
        if letter == " " and space == 1:
            decrypted_message.append(" ")

        # else calculate decrypted letter value, then append to decrypted_message
        else:
            decrypted_value = (alphabet.index(letter) - alphabet.index(key[key_count])) % 26
            decrypted_message.append(alphabet[decrypted_value].upper())

        # increment value
        key_count += 1

    return "".join(decrypted_message)


def hill_cypher_2by2_encrypt(plaintext, a, b, c, d):
    alphabet = _cypher_alphabet()
    plaintext = list(plaintext.lower())
    encrypted_message = []

    for letter in plaintext[:]:
        if letter not in alphabet:
            plaintext.remove(letter)

    # if plaintext is not divisible by 2 - append a random letter on
    if len(plaintext) % 2 != 0:
        plaintext.append(alphabet[random.randrange(0, 25)])

    # loop through plaintext - incrementing by 2
    for i in range(0, len(plaintext), 2):

        # matrix multiplication
        val1 = ((a * alphabet.index(plaintext[i])) + (b * alphabet.index(plaintext[i + 1]))) % 26
        val2 = ((c * alphabet.index(plaintext[i])) + (d * alphabet.index(plaintext[i + 1]))) % 26

        # append encrypted letters
        encrypted_message.append(alphabet[val1])
        encrypted_message.append(alphabet[val2])

    return "".join(encrypted_message).upper()


def hill_cypher_2by2_decrypt(cyphertext, a, b, c, d):
    pass

