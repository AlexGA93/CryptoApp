# Symmetric Encryption(Fernet)
# instalation --> python -m pip install cryptography
# -----------------------------------------------------------
from cryptography.fernet import Fernet


def Generate_key():
    # Generate random key each time is called
    key_generated = Fernet.generate_key()

    return key_generated


def Encryption_Message(message, key):
    message_encoded = message.encode()
    fernet = Fernet(key)  # fernet = Fernet(key_generated)
    encrypted = fernet.encrypt(message_encoded)
    return encrypted


def main(message):
    key = Generate_key()
    encripted = Encryption_Message(message, key)
    print(
        "Fernet method \nMessage: {}, \nKey: {}, \nEncriptation: {}".format(
            message, key, encripted)
    )
    return encripted
