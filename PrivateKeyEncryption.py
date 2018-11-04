# basic cryptographic code for symmetric key
# and brute force method for cracking it
# Carl Wilhjelm

import string
import random

# generate string of even length in range 20 of random characters 
def stringGen(mIn):
    n = 2*random.randint(1, mIn)
    return ''.join(random.choices(string.ascii_letters, k=n))

# generate random binary key of length param kIn
def keyGen(kIn):
    result = ""
    for i in range(kIn):
        result += str(random.randint(0,1))
    return result

# get string of ascii values of all characters of param s in binary
def strToBin(s):
    result = ""
    for char in s:
    # append binary values, formatted to preserve leading zeroes
    # and remove leading '0b' from binary representation
        result += str(format(ord(char), '#010b'))[2:]
    return result

# map string from 8-bit askii binary value
def binToStr(b):
    result = ''
    # indexing every 8 characters in the string
    for i in range(0, binSize, 8):
        # take the integer value of the string from i to i+8 and
        # represent it as a character
        result +=chr(int(b[i:i+8], 2))
    return result

def concatenateKey(size, keyIn):
    # concatenate key such that the new key is longer than the
    # origional string using, integer division,
    # then cut down its size to match, using modulo
    result = ''
    for i in range(size//k + 1):
        result += str(keyIn)
    result = result[:-(len(result)-size)]
    return result

# encryption function takes a string param
# runs xor on key repeating for length of param
# returns xor
def encrypt(m, keyIn):
    # xor the values at each index
    # return the result as a string
    result = ""
    for i in range(len(m)):
        a = int(keyIn[i])
        b = int(m[i])
        c = a ^ b
        result += str(c)
    return result

# decryption is symmetric 
def decrypt(m, keyIn):
    return encrypt(m, keyIn)


def bruteForce(encryptedMessageIn, decryptedMessageIn):
    m1 = strToBin(encryptedMessageIn)
    m2 = strToBin(decryptedMessageIn)
    size = len(m1)
    r = 2**len(m1)
    print("Beginning brute force crack")
    print("\t total possible keys = " + str(r))
    for i in range(r):
        key = str(bin(i))[2:].zfill(size)
        if i % 200000 == 0:
            print("Attempt " + str(i))
        if m2 == encrypt(m1, key):
            return key
    return "key not found"
    
# set key of random bits of length k
k = 16
key = keyGen(k)

# set maximum length of message string
m = 2
origionalString = stringGen(m)

print("Origional string = " + origionalString)

unencryptedBinaryString = strToBin(origionalString)

print("Unencrypted binary = " + unencryptedBinaryString)

binSize = len(unencryptedBinaryString)

print("length of unencrypted binary = " + str(binSize))

conKey = concatenateKey(binSize, key)

print("length of conKey = " + str(len(conKey)))

encryptedBinaryString = encrypt(unencryptedBinaryString, conKey)

print("Encrypted binery = " + encryptedBinaryString)

encryptedString = binToStr(encryptedBinaryString)

print("Encrypted string = " + encryptedString)

decryptedBinaryString = decrypt(encryptedBinaryString, conKey)

print("Decrypted binary = " + decryptedBinaryString)

decryptedString = binToStr(decryptedBinaryString)

print("Decrypted message = " + decryptedString)

bruteForceKey = bruteForce(origionalString, encryptedString)

print("Brute force key = " + bruteForceKey)
print("Original key    = " + conKey)
