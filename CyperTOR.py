import random


def _cypher_alphabet():
    return list('abcdefghijklmnopqrstuvwxyz')


def _calculate_determinant(matrix):
    determinant = 1 / ((matrix[0] * matrix[3]) - (matrix[1] * matrix[2]))


def hill_cypher_2by2_encrypt(plaintext, a, b, c, d):
    alphabet = _cypher_alphabet()
    plaintext = list(plaintext.lower())
    encrypted_message = []

    for letter in plaintext[:]:
        if letter not in alphabet:
            plaintext.remove(letter)

    # if plaintext is not divisible by 2 - append a random letter on
    if len(plaintext) % 2 != 0:
        plaintext.append(alphabet[random.randrange(0, 25)])

    # loop through plaintext - incrementing by 2
    for i in range(0, len(plaintext), 2):

        # matrix multiplication
        val1 = ((a * alphabet.index(plaintext[i])) + (b * alphabet.index(plaintext[i + 1]))) % 26
        val2 = ((c * alphabet.index(plaintext[i])) + (d * alphabet.index(plaintext[i + 1]))) % 26

        # append encrypted letters
        encrypted_message.append(alphabet[val1])
        encrypted_message.append(alphabet[val2])

    return "".join(encrypted_message).upper()


def hill_cypher_2by2_decrypt(cyphertext, a, b, c, d):
    alphabet = _cypher_alphabet()
    cyphertext = list(cyphertext.lower())
    decrypted_message = []

    inverse_matrix = [d, -b, -c, a]
