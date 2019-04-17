import hashlib

def hashing_methods(password_hash):
    #Hashing methods
    hash_md5 = hashlib.md5(password_hash.encode())
    hash_sha1 = hashlib.sha1(password_hash.encode())
    hash_sha224 = hashlib.sha224(password_hash.encode())
    hash_sha256 = hashlib.sha256(password_hash.encode())
    hash_sha384 = hashlib.sha384(password_hash.encode())
    hash_sha512 = hashlib.sha512(password_hash.encode())

    md5_digest = hash_md5.hexdigest()
    sha1_digest = hash_sha1.hexdigest()
    sha224_digest = hash_sha224.hexdigest()
    sha256_digest = hash_sha256.hexdigest()
    sha384_digest = hash_sha384.hexdigest()
    sha512_digest = hash_sha512.hexdigest()

    #Type = tuple
    output = (" Input:  ", password_hash,
              "\n Output: \nmd5: ",md5_digest,
              "\n sha1: ",sha1_digest,
              "\n sha224: ",sha224_digest,
              "\n sha256: ",sha256_digest,
              "\n sha384: ",sha384_digest, 
              "\n sha512: ",sha512_digest)

    #convert tuple to string
    str = ''.join(output)
    
    #Add method to create a file as backup to save info

    print(str)
    return str




def main():
    password_hash = input('Password: ')#GUI Input
    hashing_methods(password_hash)


if __name__ == "__main__":
    main()