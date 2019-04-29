
import base64
import pyaes
import random
from Cryptodome import Random
from Cryptodome.Cipher import AES


def encrypt(key, plaintxt):
    aes = pyaes.AESModeOfOperationCTR(key)
    message = aes.encrypt(plaintxt)
    return message


if __name__ == '__main__':
    # 32 bytes key
    key = ''.join(chr(random.randint(0, 0x7e))for i in range(32))
    print('key: '+key)
    key_encoded = key.encode('utf8')

    # plaintext generation(a - z) with any length you wish
    plaintext = ''.join(chr(random.randint(61, 0x7a)))

    result = encrypt(key_encoded, plaintext)#FINAL DATA
    

