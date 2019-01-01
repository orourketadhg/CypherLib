# Author: Tadhg O'Rourke
# Created: 23/12/2018
# Last Edited: 23/12/2018

# Title: Testing cyphers

from cypher.Caesar import Caesar
from cypher.Vigenere import Vigenere
from cypher.Atbash import Atbash
from cypher.ROT13 import ROT13

print("=" * 50, end='\n\n')

print("Caesar Cypher Testing: ")

caesar_cypher = Caesar()

caesar_encrypt = caesar_cypher.encrypt("Hello World", 15)
print("Encrypted - " + caesar_encrypt, end='\n\n')

caesar_decrypt = caesar_cypher.decrypt(caesar_encrypt, 15)
print("Decrypted - " + caesar_decrypt, end='\n\n')

print("=" * 50, end='\n\n')

print("Vigenere Cypher Testing:")

vigenere_cypher = Vigenere()

vigenere_encrypt = vigenere_cypher.encrypt("Hello World", "test")
print("Encrypted - " + vigenere_encrypt, end='\n\n')

vigenere_decrypt = vigenere_cypher.decrypt(vigenere_encrypt, "test")
print("Decrypted - " + vigenere_decrypt, end='\n\n')

print("=" * 50, end='\n\n')

print("Atbash Cypher Testing:")

atbash_cypher = Atbash()

atbash_encrypt = atbash_cypher.encrypt("Hello World", "zabcdefghijklmonpqrstuvwxy")
print("Encrypted - " + atbash_encrypt, end='\n\n')

atbash_decrypt = atbash_cypher.decrypt(atbash_encrypt, "zabcdefghijklmonpqrstuvwxy")
print("Decrypted - " + atbash_decrypt, end='\n\n')

print("=" * 50, end='\n\n')

print("ROT13 Cypher Testing:")

ROT13_cypher = ROT13()

ROT13_encrypt = ROT13_cypher.encrypt("Hello World")
print("Encrypted - " + ROT13_encrypt, end='\n\n')

ROT13_decrypt = ROT13_cypher.decrypt(ROT13_encrypt)
print("Decrypted - " + ROT13_decrypt, end='\n\n')

print("=" * 50, end='\n\n')

