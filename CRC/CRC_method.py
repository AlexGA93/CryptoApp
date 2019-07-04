def polynomialMethod(key):
    # interpreting polynomial's base
    base = int(key[0])

    binary = ""
    i = 0

    for j in range(base, -1, -1):  # Iterations = polynomial'sindex
        if j == int(key[i]):
            binary += "1"
            i += 1
        else:
            binary += "0"

    return binary  # return polynomial's binary form


def xorFunc(plot, pol):
    resul = []

    for i in range(0, len(pol)-1):

        if plot[i] == pol[i]:

            resul.append('0')
        else:
            resul.append('1')

    return ''.join(resul)


def divFunc(divident, divisor):
    lmessage = len(divident)
    lkey = len(divisor)

    # Taking first bits as our divisor's length
    tmp = divident[0:lkey]

    while lkey < lmessage:

        if tmp[0] == "1":
            # updating tmp's value
            tmp = xorFunc(divisor, tmp) + divident[lkey]
        else:
            tmp = xorFunc(tmp, '0'*lkey) + divident[lkey]

        lkey += 1

    if tmp[0] == '1':
        tmp = xorFunc(tmp, divisor)
    else:
        tmp = xorFunc('0'*lkey, tmp)

    return tmp


def CRC(mssgBin, keyBin):
    long = len(keyBin)
    # adding 0s as key's len
    attached = mssgBin + '0'*(long-1)
    # binary division using Xor gates
    final_data = divFunc(attached, keyBin)

    return final_data


def main(message, key):
    key_str = str(key)
    # convert message into binary
    messageBin = ''.join(format(ord(x), 'b')for x in message)

    # Generate a polynomial to work with
    polynomial = polynomialMethod(key_str)

    final_data = CRC(messageBin, polynomial)

    return final_data
