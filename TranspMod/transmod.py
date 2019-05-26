def main():
    #message to encrypt
    message = 'Hi my name is Alejandro' # len(message) > key
    print(message)
    #key
    key = 5 # key*key matrix
    #function
    ciphertext = encryption(message,key)

    print(ciphertext)

def encryption(message,key):
    #each string represents a matrix column
    ciphermessage = ['']*key #key spaces vector                 
    l = len(message)
    #matrix
    '''
    For each col we operate if the pointer < len(message)

    if not... next col
    '''
    for col in range(key):                   
        pointer = col
        
        #reading column's element
        while pointer<l:
        
            ciphermessage[col]+=message[pointer]
            
            #pointer to the next column element
            pointer+=key

    #list into string and return        
    return ''.join(ciphermessage)

if __name__=="__main__":
    main()