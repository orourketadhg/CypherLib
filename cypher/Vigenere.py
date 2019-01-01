# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 01/01/2019

# Title: vigenere cypher

from cypher.General import Cypher


class Vigenere(Cypher):

    def __init__(self):
        self.alphabet = self.alphabet_lower()
        self.new_message = []

    def encrypt(self, plaintext, key):
        plaintext = list(plaintext.lower())
        key = list(key)
        self.new_message = []

        # reset key_count
        key_count = 0

        # loop through plaintext
        for letter in plaintext:

            #  if key_count at length of key - reset to zero
            if key_count == len(key):
                key_count = 0

            # if letter is a space and in space mode - append a space
            if letter == ' ':
                self.new_message.append(" ")

            # elif non alphabetical char - continue
            elif letter not in self.alphabet:
                continue

            # else alphabetical char - append encrypted letter
            else:
                # calculate encrypted letter value
                encrypted_value = (self.alphabet.index(letter) + self.alphabet.index(key[key_count])) % 26

                # append encrypted letter
                self.new_message.append(self.alphabet[encrypted_value].upper())

            # increment key_count
            key_count += 1

        # return encrypted string
        return "".join(self.new_message)

    def decrypt(self, cyphertext, key):
        cyphertext = list(cyphertext.lower())
        key = list(key)
        self.new_message = []

        # reset key_count
        key_count = 0

        # loop through cyphertext
        for letter in cyphertext:

            # if key_count at max length - set to zero
            if key_count == len(key):
                key_count = 0

            # if letter is a space and space mode enabled - append a space
            if letter == " ":
                self.new_message.append(" ")

            # else - append decrypted letter
            else:
                # calculate decrypted value
                decrypted_value = (self.alphabet.index(letter) - self.alphabet.index(key[key_count])) % 26

                # append decrypted letter
                self.new_message.append(self.alphabet[decrypted_value].upper())

            # increment value
            key_count += 1

        # return decrypted string
        return "".join(self.new_message)


# methods wont work unless imported
if __name__ == '__name__':
    print("Import cypher to gain use of cyphers")
