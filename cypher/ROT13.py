# Author: Tadhg O'Rourke
# Created: 01/01/2019
# Last Edited: 01/01/2019

# Title: ROT13 Cypher
from cypher.General import Cypher


class ROT13(Cypher):

    def __init__(self):
        self.alphabet = self.alphabet_lower()
        self.new_message = []
        self.offset = 13

    def encrypt(self, plaintext):
        plaintext = list(plaintext.lower())
        self.new_message = []

        # loop through letters in plaintext
        for letter in plaintext:

            # if letter is a space - append space
            if letter == " ":
                self.new_message.append(" ")

            # elif letter is not in known alphabet - skip letter
            elif letter not in self.alphabet:
                continue

            # elif letter is known - append encrypted letter
            elif letter in self.alphabet:
                # get letter index value
                letter_value = self.alphabet.index(letter)

                # calculate encrypted letter value
                offset_value = (letter_value + self.offset) % 26

                # append encrypted letter
                self.new_message.append(self.alphabet[offset_value].upper())

        # return encrypted string
        return ''.join(self.new_message)

    def decrypt(self, cyphertext):
        cyphertext = list(cyphertext.lower())
        self.new_message = []

        # loop through cyphertext
        for letter in cyphertext:

            # if letter is a space - append space
            if letter == " ":
                self.new_message.append(" ")

            # elif letter is not in known alphabet - skip letter
            elif letter not in self.alphabet:
                continue

            # else - append decrypted letter
            else:
                # get encrypted letter value index
                letter_value = self.alphabet.index(letter)

                # calculate decrypted letter value
                offset_value = (letter_value - self.offset) % 26

                # append encrypted letter
                self.new_message.append(self.alphabet[offset_value].upper())

        # return encrypted string
        return ''.join(self.new_message)


# methods wont work unless imported
if __name__ == '__name__':
    print("Import cypher to gain use of cyphers")