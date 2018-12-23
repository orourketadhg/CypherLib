# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 23/12/2018

# Title: Atbash Cypher

from cypher.General import Cypher


class Atbash(Cypher):

    def __init__(self):
        self.alphabet = self.alphabet_lower()
        self.new_message = []

    def encrypt(self, plaintext, alphabet_key):
        self.new_message = []
        plaintext = list(plaintext.lower())
        alphabet_key = list(alphabet_key.lower())

        for letter in plaintext:

            if letter == " ":
                self.new_message.append(" ")

            elif letter not in alphabet_key:
                raise "Letter {} not in passed encryption alphabet".format(letter)

            else:
                value = self.alphabet.index(letter)
                self.new_message.append(alphabet_key[value])

        return "".join(self.new_message).upper()

    def decrypt(self, cyphertext, alphabet_key):
        self.new_message = []
        cyphertext = list(cyphertext.lower())
        alphabet_key = list(alphabet_key.lower())

        for letter in cyphertext:

            if letter == ' ':
                self.new_message.append(" ")

            elif letter not in alphabet_key:
                raise "Letter {} not in passed encryption alphabet".format(letter)

            else:
                value = alphabet_key.index(letter)
                self.new_message.append(self.alphabet[value])

        return "".join(self.new_message).upper()
