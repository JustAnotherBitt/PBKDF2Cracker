# PBKDF2 Hash Cracker

This Python script attempts to recover a password by brute-forcing a given PBKDF2-HMAC-SHA256 hash using a dictionary attack. It iterates through a wordlist, hashing each word with the specified salt and comparing it to the target hash.

## Requirements
- Python 3
- A wordlist file (e.g., `rockyou.txt`)

## Usage
1. Modify the script to set your desired `salt` and `target_hash`.
2. Ensure you have a valid dictionary file (wordlist) and update `dictionary_file` in the script.
3. Run the script:
   
   ```sh
   python script.py
   ```

## Example

```python
salt = binascii.unhexlify('8bf3e3452b78544f8bee9400d6936d34')
target_hash = 'e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56'
dictionary_file = '/usr/share/wordlists/rockyou.txt'
find_matching_password(dictionary_file, target_hash, salt)
```

## Notes
- Changing the salt will result in completely different hashes.
- Ensure the wordlist contains the password, or the script won't find a match.
- The number of iterations (`50000` by default) can be adjusted for stronger security.
