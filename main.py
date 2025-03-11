import hashlib
import binascii
 
def pbkdf2_hash(password, salt, iterations=50000, dklen=50):
    hash_value = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        iterations,
        dklen
    )
    return hash_value
 
def find_matching_password(dictionary_file, target_hash, salt, iterations=50000, dklen=50):
    target_hash_bytes = binascii.unhexlify(target_hash)
    
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            password = line.strip()
            hash_value = pbkdf2_hash(password, salt, iterations, dklen)
            count += 1
            print(f"Testing {count}: {password}")
            if hash_value == target_hash_bytes:
                print(f"\nFound password: {password}")
                return password
        print("Password not found.")
        return None
 
salt = binascii.unhexlify('8bf3e3452b78544f8bee9400d6936d34') # change it?
target_hash = 'e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56' # change it
dictionary_file = '/usr/share/wordlists/rockyou.txt' # change it??
find_matching_password(dictionary_file, target_hash, salt)