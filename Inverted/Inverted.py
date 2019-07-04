

def toBinary(message):
    # Turn to str
    m_bin = ' '.join(format(ord(x), 'b') for x in message)
    # conversion to list
    bynary_array = m_bin.split()

    for i, element in enumerate(bynary_array):
        if element == '100000':
            bynary_array[i] = ' '

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
    print(
        "Inverted method \nMessage: {}, \nEncriptation: {}".format(
            message, string_inverted)
    )
    return string_inverted
