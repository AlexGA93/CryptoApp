# Mono-alphabetic substitution coding
# Security level: Low


# importing message from INDEX.PY
def Atbash_encrypt(alpha, crypto, message):
    c_message = ""
    for n in message.lower():
        if n in alpha:
            pos = alpha.index(n)
            ncrypt = crypto[pos]
            c_message += ncrypt
        else:
            ncrypt += n
    return c_message


def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cryptoalpha = alpha[::-1]  # inverted alpha
    cryptoalpha = cryptoalpha.upper()

    message = "Hello World"  # message from INDEX.PY

    # calling function
    encryption = Atbash_encrypt(alpha, cryptoalpha, message)
    #print("GUI text: {}".format(message))
    print("Encrypted text: {}".format(encryption))


if __name__ == "__main__":
    main()
