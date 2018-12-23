# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 23/12/2018

# Title: general methods for all ciphers


class Cypher:

    @staticmethod
    def alphabet_lower():
        return list("abcdefghijklmonpqrstuvwxyz")

    @staticmethod
    def alphabet_capital():
        return list("abcdefghijklmonpqrstuvwxyz".upper())


if __name__ == '__name__':
    print("Import cypher to gain use of cyphers")
