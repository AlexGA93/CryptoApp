# Symmetric Encryption(Fernet)
# instalation --> python -m pip install cryptography
# -----------------------------------------------------------
from cryptography.fernet import Fernet


def Generate_key():
    # Generate random key each time is called
    key_generated = Fernet.generate_key()
    # print(key)
    # Saving the key into a file (byte type)
    file_write = open('key.key', 'wb')
    file_write.write(key_generated)
    file_write.close()  # putting key into the file created and close


def Read_key():
    # Reading key from byte file
    file_read = open('key.key', 'rb')
    key_readed = file_read.read()
    file_read.close()

    return key_readed


def Encryption_Message(message):
    message_encoded = message.encode()
    f = Fernet(Read_key())
    encrypted = f.encrypt(message_encoded)

    return encrypted


def Decryption_Message(key_generated, encripted):
    f2 = Fernet(key_generated)
    decrypted = decrypted = f2.decrypt(encripted)  # Bytes object

    original_message = decrypted.decode()  # turn object into a string

    return original_message


if __name__ == '__main__':
    Generate_key()
    key_generated = Read_key()

    message = "Example string"
    encripted = Encryption_Message(message)

    decripted = Decryption_Message(key_generated, encripted)
    
