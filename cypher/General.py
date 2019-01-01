# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 01/01/2019

# Title: general methods for all ciphers


class Cypher:

    # method to return a list of all lower case letters
    @staticmethod
    def alphabet_lower():
        return list("abcdefghijklmonpqrstuvwxyz")

    # method to return a list of all upper case letters
    @staticmethod
    def alphabet_capital():
        return list("abcdefghijklmonpqrstuvwxyz".upper())


# methods wont work unless imported
if __name__ == '__name__':
    print("Import cypher to gain use of cyphers")
