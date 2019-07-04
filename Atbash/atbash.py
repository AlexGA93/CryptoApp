# Mono-alphabetic substitution coding
# Security level: Low


# importing message from INDEX.PY
def Atbash_encrypt(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cryptoalpha = alpha[::-1]  # inverted alpha
    cryptoalpha = cryptoalpha.upper()

    c_message = ""
    for n in message.lower():
        if n in alpha:
            pos = alpha.index(n)
            ncrypt = cryptoalpha[pos]
            c_message += ncrypt
        else:
            ncrypt += n

    print(
        "Atbash method \nMessage: {}, \nEncriptation: {}".format(
            message, c_message)
    )
    return c_message
