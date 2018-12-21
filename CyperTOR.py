"""
Author: Tadhg O'Rourke
Date: 20/12/2018

Project Description:
"""


def _cypher_alphabet():
    return 'abcdefghijklmnopqrstuvwxyz'


def caesar_cypher_encrypt(plaintext, offset):
    alphabet_split = list(_cypher_alphabet())
    plaintext_split = list(plaintext.lower())
    unknown_letter = []
    encrypted_message = []

    # loop through letters in plaintext
    for letter in plaintext_split:

        # if letter is a space
        if letter == " ":
            encrypted_message.append(" ")
            continue

        # elif letter is not in known alphabet
        elif letter not in alphabet_split:
            # add letter to unknown letters
            unknown_letter.append(letter)
            continue

        # if letter is known
        elif letter in alphabet_split:
            letter_value = alphabet_split.index(letter)
            encrypted_value = (letter_value + offset) % 26
            encrypted_message.append(alphabet_split[encrypted_value].upper())

    return ''.join(encrypted_message)


def caesar_cypher_decrypt(cyphertext, offset):
    alphabet_split = list(_cypher_alphabet())
    cyphertext_split = list(cyphertext.lower())
    decrypted_message = []

    # loop through cyphertext
    for letter in cyphertext_split:

        # if letter is a space
        if letter == " ":
            decrypted_message.append(" ")
            continue

        # decrypt letter to get value
        else:
            letter_value = alphabet_split.index(letter)
            decrypted_value = (letter_value - offset) % 26
            decrypted_message.append(alphabet_split[decrypted_value].upper())

    return ''.join(decrypted_message)


def hill_cypher_2by2_encrypt(plaintext, a, b, c, d):
    pass


def hill_cypher_2by2_decrypt(cyphertext, a, b, c, d):
    pass


def vigenere_cypher_encrypt(plaintext, key):
    pass


def vigenere_cypher_decrypt(cyphertext, key):
    pass
