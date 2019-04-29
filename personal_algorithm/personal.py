

def toBinary(mensaje):
    # conversion to str
    mensaje_binario = ' '.join(format(ord(x), 'b') for x in mensaje)
    # conversion to list
    bynary_array = mensaje_binario.split()

    for i, element in enumerate(bynary_array):
        if element == '100000':
            bynary_array[i] = ' '

    # print(bynary_array)  # list

    # converting list to string
    string_array = ''.join(map(str, bynary_array))
    print(string_array)

    string_inverted = ''
    for x in string_array:
        if x == '1':
            string_inverted += '0'
        elif x == '0':
            string_inverted += '1'
        elif x == ' ':
            string_inverted += ' '

    # string_inverted
    return string_inverted


if __name__ == "__main__":
    mensaje = 'Hello World'#INPUT
    final_data = toBinary(mensaje)#FINAL DATA
