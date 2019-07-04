def encryption(message, key):
    # each string represents a matrix column
    ciphermessage = ['']*key  # key spaces vector
    lenght = len(message)
    '''
    For each col we operate if the pointer < len(message)
    if not... next col
    '''
    for col in range(key):
        pointer = col
        # reading column's element
        while pointer < lenght:
            ciphermessage[col] += message[pointer]
            # pointer to the next column element
            pointer += key
    # list into string and return
    print(
        "Transmod method \nMessage: {}, \nKey: {}, \nEncriptation: {}".format(
            message, key, ciphermessage)
    )
    return ''.join(ciphermessage)
