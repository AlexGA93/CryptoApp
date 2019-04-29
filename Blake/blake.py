'''
Optimized for 64-bit platforms and produces digests of any size between 1 and 64 bytes.

hashlib.blake2b(data=b'', *, digest_size=64, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False)

These functions return the corresponding hash objects for calculating BLAKE2b or BLAKE2s. They optionally take these general parameters:

data: initial chunk of data to hash, which must be bytes-like object. It can be passed only as positional argument.
digest_size: size of output digest in bytes.
key: key for keyed hashing (up to 64 bytes for BLAKE2b, up to 32 bytes for BLAKE2s).
salt: salt for randomized hashing (up to 16 bytes for BLAKE2b, up to 8 bytes for BLAKE2s).
person: personalization string (up to 16 bytes for BLAKE2b, up to 8 bytes for BLAKE2s).

'''

from hashlib import blake2b, blake2s


def encrypt_blake2b(message, size):

    blake2b_variable = blake2b(digest_size=size)
    blake2b_variable.update(message.encode())
    encrypted_2b = blake2b_variable.hexdigest()

    #print(encrypted_2b)
    return encrypted_2b


def encrypt_blake2s(message, size):
    blake2s_variable = blake2s(digest_size=size)
    blake2s_variable.update(message.encode())
    encrypted_2s = blake2s_variable.hexdigest()

    #print(encrypted_2s)

    return encrypted_2s

def data_returned(blake_2b, blake_2s):
    data = ("Blake Encryption: \n"+"Blake2b: "+ blake_2b+"\nBlake2s: "+blake_2s)
    return data

if __name__ == "__main__":

    string = 'Prueba'
    size = 20

    blake_2b = encrypt_blake2b(string, size)
    blake_2s = encrypt_blake2s(string, size)

    data_returned(blake_2b, blake_2s)
