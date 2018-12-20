"""
Author: Tadhg O'Rourke
Date: 20/12/2018

Project Description:
"""


def _cypher_alphabet():
    return 'abcdefghijklmnopqrstuvwxyz'


def ceaser_cypher_encrypt(plaintext, offset):
    alphabet_split = list(_cypher_alphabet())
    alphabet = _cypher_alphabet()
    plaintext_split = list(plaintext.lower())
    unknown_letter = []
    encrypted_message = []

    # loop through letters in plaintext
    for letter in plaintext_split:
        print(letter)

        # if letter is not in known alphabet
        if letter not in alphabet:
            # add letter to unknown letters
            unknown_letter.append(letter)
            continue

        # if letter is known
        elif letter in alphabet:
            letter_value = alphabet.index(letter)
            encrypted_value = (letter_value + offset) % 26
            encrypted_message.append(alphabet_split[encrypted_value])

    print(''.join(encrypted_message))


def ceaser_cypher_decrypt(cyphertext, offset):
    pass


def hill_cypher_2by2_encrypt(plaintext, a, b, c, d):
    pass


def hill_cypher_2by2_decrypt(cyphertext, a, b, c, d):
    pass


def vigenere_cypher_encrypt(plaintext, key):
    pass


def vigenere_cypher_decrypt(cyphertext, key):
    pass
