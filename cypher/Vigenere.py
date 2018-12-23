# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 23/12/2018

# Title: vigenere cypher

from cypher.General import Cypher


class Vigenere(Cypher):

    def __init__(self):
        self.alphabet = self.alphabet_lower()
        self.new_message = []
        self.key_count = 0

    def encrypt(self, plaintext, key):
        plaintext = list(plaintext.lower())
        key = list(key)
        self.new_message = []

        self.key_count = 0

        # loop through plaintext
        for letter in plaintext:

            #  if key_count at length of key reset to zero
            if self.key_count == len(key):
                self.key_count = 0

            # if letter is a space and in space mode - append a space
            if letter == ' ':
                self.new_message.append(" ")

            # elif non alphabetical char - continue
            elif letter not in self.alphabet:
                continue

            # else alphabetical char - calculate value, append alphabet letter matching value
            else:
                encrypted_value = (self.alphabet.index(letter) + self.alphabet.index(key[self.key_count])) % 26
                self.new_message.append(self.alphabet[encrypted_value].upper())

            # increment key_count
            self.key_count += 1

        return "".join(self.new_message)

    def decrypt(self, cyphertext, key):
        cyphertext = list(cyphertext.lower())
        key = list(key)
        self.new_message = []

        self.key_count = 0

        # loop through cyphertext
        for letter in cyphertext:

            # if key_count at max length - set to zero
            if self.key_count == len(key):
                self.key_count = 0

            # if letter is a space and space mode enabled - append a space
            if letter == " ":
                self.new_message.append(" ")

            # else calculate decrypted letter value, then append to decrypted_message
            else:
                decrypted_value = (self.alphabet.index(letter) - self.alphabet.index(key[self.key_count])) % 26
                self.new_message.append(self.alphabet[decrypted_value].upper())

            # increment value
            self.key_count += 1

        return "".join(self.new_message)
