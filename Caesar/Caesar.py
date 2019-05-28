# importing module.py
# import message_to_code


# importing index's entry value
# from ... import index


def caesar(data, key):
    encryptMessage = ''
    for x in data:
        if x == ' ':
            encryptMessage += ' '
        chr_to_Ascii = ord(x)
        if(chr_to_Ascii >= 65 and chr_to_Ascii <= 90):  # upper
            Ascii_to_Uchr = chr(chr_to_Ascii+key)

            if (ord(Ascii_to_Uchr) > 90):
                Ascii_to_Uchr = chr(97)
            encryptMessage += Ascii_to_Uchr

        elif(chr_to_Ascii >= 97 and chr_to_Ascii <= 122):  # lower
            Ascii_to_Lchr = chr(chr_to_Ascii+key)
            if ord(Ascii_to_Lchr) > 122:
                Ascii_to_Lchr = chr(65)
            encryptMessage += Ascii_to_Lchr

    
    return encryptMessage


