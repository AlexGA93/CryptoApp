'''
import base64
import pyaes
import random
from Cryptodome import Random
from Cryptodome.Cipher import AES

key = ''.join(chr(random.randint(0,0x7e))for i in range(32))
key_encoded = key.encode('utf8')


plaintext = ''.join(chr(random.randint(61,0x7a)))

aes = pyaes.AESModeOfOperationCTR(key_encoded)

message = aes.encrypt(plaintext)
print(message)
'''
def hola():
    print('hola')

hola()