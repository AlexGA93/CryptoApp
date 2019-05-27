
import base64
import pyaes
import random
from Cryptodome import Random
from Cryptodome.Cipher import AES


def encrypt():
    # 32 bytes key
    key = ''.join(chr(random.randint(0, 0x7e))for i in range(32))
    #print('key: '+key)
    key_encoded = key.encode('utf8')

    # plaintext generation(a - z) with any length you wish
    plaintext = ''.join(chr(random.randint(61, 0x7a)))

    aes = pyaes.AESModeOfOperationCTR(key_encoded)

    message = aes.encrypt(plaintext)
    return message


def main():
    result = encrypt()  # FINAL DATA
    #print("resultado: {}".format(result))


if __name__ == '__main__':
    main()
