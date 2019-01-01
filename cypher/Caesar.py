# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 01/01/2019

# Title: caesar cypher

from cypher.General import Cypher


class Caesar(Cypher):

    def __init__(self):
        self.alphabet = self.alphabet_lower()
        self.new_message = []
        self.offset_value = 0

    def encrypt(self, plaintext, offset):
        plaintext_split = list(plaintext.lower())
        self.new_message = []

        # loop through letters in plaintext
        for letter in plaintext_split:

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
                self.offset_value = (letter_value + offset) % 26

                # append encrypted letter
                self.new_message.append(self.alphabet[self.offset_value].upper())

        # return encrypted string
        return ''.join(self.new_message)

    def decrypt(self, cyphertext, offset):
        cyphertext_split = list(cyphertext.lower())
        self.new_message = []

        # loop through cyphertext
        for letter in cyphertext_split:

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
                self.offset_value = (letter_value - offset) % 26

                # append encrypted letter
                self.new_message.append(self.alphabet[self.offset_value].upper())

        # return encrypted string
        return ''.join(self.new_message)


# methods wont work unless imported
if __name__ == '__name__':
    print("Import cypher to gain use of cyphers")
