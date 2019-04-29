import hashlib
import binascii


def hashing_methods(password_hash):
    # All Hashing methods
    hash_md5 = hashlib.md5(password_hash.encode())
    hash_sha1 = hashlib.sha1(password_hash.encode())
    hash_sha224 = hashlib.sha224(password_hash.encode())
    hash_sha256 = hashlib.sha256(password_hash.encode())
    hash_sha384 = hashlib.sha384(password_hash.encode())
    hash_sha512 = hashlib.sha512(password_hash.encode())

    iterations = 100000
    kd = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', iterations)
    key_deri = binascii.hexlify(kd)

    # key_derivation = str(key_deri)
    # print(key_derivation)

    md5_digest = hash_md5.hexdigest()
    sha1_digest = hash_sha1.hexdigest()
    sha224_digest = hash_sha224.hexdigest()
    sha256_digest = hash_sha256.hexdigest()
    sha384_digest = hash_sha384.hexdigest()
    sha512_digest = hash_sha512.hexdigest()

    # Type = tuple
    output = (" Input:  ", password_hash,
              "\n Output: \n md5: ", md5_digest,
              "\n sha1: ", sha1_digest,
              "\n sha224: ", sha224_digest,
              "\n sha256: ", sha256_digest,
              "\n sha384: ", sha384_digest,
              "\n sha512: ", sha512_digest)

    # convert tuple to string
    str = ''.join(output)
    # convert key derivation into string
    k_d = key_deri.decode("utf-8")

    result = str+"\n key derivation: "+k_d

    print(result)
    return result


def main():
    password_hash = input('Password: ')  # GUI Input
    final_data = hashing_methods(password_hash)#FINAL DATA


if __name__ == "__main__":
    main()
