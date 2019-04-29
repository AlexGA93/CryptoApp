# importing module.py
# import message_to_code

# caesar function


def caesar(data, order):
    message = ''
    for x in data:
        if x == ' ':
            message += ' '
        chr_to_Ascii = ord(x)
        if(chr_to_Ascii >= 65 and chr_to_Ascii <= 90):
            Ascii_to_Uchr = chr(chr_to_Ascii+order)
            if (ord(Ascii_to_Uchr) > 90):
                Ascii_to_Uchr = chr(97)
            message += Ascii_to_Uchr

        elif(chr_to_Ascii >= 97 and chr_to_Ascii <= 122):  # trabajamos con minusculas
            Ascii_to_Lchr = chr(chr_to_Ascii+order)
            if ord(Ascii_to_Lchr) > 122:
                Ascii_to_Lchr = chr(65)
            message += Ascii_to_Lchr
    
    return message
# Caesar Decipher def

'''
def NonCaesar(data, order):
    message = ''

    for x in data:
        if x == ' ':
            message += ' '
        chr_to_Ascii = ord(x)
        if(chr_to_Ascii >= 65 and chr_to_Ascii <= 90):
            Ascii_to_Uchr = chr(chr_to_Ascii-order)
            if (ord(Ascii_to_Uchr) > 90):
                Ascii_to_Uchr = chr(97)
            message += Ascii_to_Uchr

        elif(chr_to_Ascii >= 97 and chr_to_Ascii <= 122):  # trabajamos con minusculas
            Ascii_to_Lchr = chr(chr_to_Ascii-order)
            if ord(Ascii_to_Lchr) > 122:
                Ascii_to_Lchr = chr(65)
            message += Ascii_to_Lchr
    print(message)
    return message
 '''   


def code():
    message = input('Give me a message: ')#input message GUI
    order = int(input('Give me a order number to cipher: ')) #input integer GUI
    return(caesar(message, order))
    '''
    option = input('What do you want to do? Cipher[C] or Decipher[D]? ')
    if option == 'C':
        caesar(message, order)
    elif option == 'D':
        NonCaesar(message, order)
    else:
        print('This code only admits the two last options.')
'''
if __name__ == "__main__":
    final_data = code()
    print(final_data)
