import hashlib
import binascii


def hashing_methods(message, iterations):
    # All Hashing methods
    hash_md5 = hashlib.md5(message.encode())
    hash_sha1 = hashlib.sha1(message.encode())
    hash_sha224 = hashlib.sha224(message.encode())
    hash_sha256 = hashlib.sha256(message.encode())
    hash_sha384 = hashlib.sha384(message.encode())
    hash_sha512 = hashlib.sha512(message.encode())

    kd = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', iterations)
    key_deri = binascii.hexlify(kd)

    md5_digest = hash_md5.hexdigest()
    sha1_digest = hash_sha1.hexdigest()
    sha224_digest = hash_sha224.hexdigest()
    sha256_digest = hash_sha256.hexdigest()
    sha384_digest = hash_sha384.hexdigest()
    sha512_digest = hash_sha512.hexdigest()

    # Type = tuple
    output = (" Input:  ", message,
              "\n Output: \nMD5:\n", md5_digest,
              "\n SHA1:\n ", sha1_digest,
              "\n SHA224:\n ", sha224_digest,
              "\n SHA256:\n ", sha256_digest,
              "\n SHA384:\n ", sha384_digest,
              "\n SHA512:\n ", sha512_digest)

    # convert tuple to string
    str_data = ''.join(output)
    # convert key derivation into string
    k_d = key_deri.decode("utf-8")

    result = str_data+"\n key derivation: \n"+k_d

    print(
        "Hash method \nMessage: {}, \nIterations: {},  \nEncriptation: {}".format(
            message, iterations, result)
    )

    return result
