# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 23/12/2018

# Title: Testing cyphers

from cypher.Caesar import Caesar
from cypher.Vigenere import Vigenere

print("=" * 50, end='\n\n')

print("Caesar Cypher Testing", end='\n\n')

caesar_cypher = Caesar()

caesar_encrypt = caesar_cypher.encrypt("Hello World", 15)
print(caesar_encrypt, end='\n\n')

caesar_decrypt = caesar_cypher.decrypt(caesar_encrypt, 15)
print(caesar_decrypt, end='\n\n')

print("=" * 50, end='\n\n')

print("Vigenere Cypher Testing")

vigenere_cypher = Vigenere()

vigenere_encrypt = vigenere_cypher.encrypt("Hello World", "test")
print(vigenere_encrypt, end='\n\n')

vigenere_decrypt = vigenere_cypher.decrypt(vigenere_encrypt, "test")
print(vigenere_decrypt, end='\n\n')
