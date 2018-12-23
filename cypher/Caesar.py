# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 23/12/2018

# Title: caesar cypher

from cypher.General import Cipher


class Caesar(Cipher):

    def __init__(self):
        self.alphabet = self.alphabet_lower()
        self.new_message = []
        self.offset_value = 0

    def encrypt(self, plaintext, offset):
        plaintext_split = list(plaintext.lower())

        # loop through letters in plaintext
        for letter in plaintext_split:

            # if letter is a space
            if letter == " ":
                self.new_message.append(" ")

            # elif letter is not in known alphabet
            elif letter not in self.alphabet:
                continue

            # if letter is known
            elif letter in self.alphabet:
                letter_value = self.alphabet.index(letter)
                self.offset_value = (letter_value + offset) % 26
                self.new_message.append(self.alphabet[self.offset_value].upper())

        return ''.join(self.new_message)

    def decrypt(self, cyphertext, offset):
        cyphertext_split = list(cyphertext.lower())

        # loop through cyphertext
        for letter in cyphertext_split:

            # if letter is a space
            if letter == " ":
                self.new_message.append(" ")

            # decrypt letter to get value
            else:
                letter_value = self.alphabet.index(letter)
                self.offset_value = (letter_value - offset) % 26
                self.new_message.append(self.alphabet[self.offset_value].upper())

        return ''.join(self.new_message)


if __name__ == '__main__':
    print("Import cypher to gain use of cyphers")
