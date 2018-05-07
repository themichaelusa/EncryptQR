"""
Blocksize Legend
BS = 16 (AES-128)
BS = 24 (AES-192)
BS = 32 (AES-256)
"""

class AES:
    def __init__(self, key, BS=16):
        import hashlib
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.unpad = lambda s: s[0:-(s[-1])]

    def encrypt(self, raw):
        import base64
        from Crypto import Random
        from Crypto.Cipher import AES

        raw = self.pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        import base64
        from Crypto import Random
        from Crypto.Cipher import AES

        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))

"""
Test AES

if __name__ == "__main__": 
    cipher = AES('mysecretpassword', BS=16)
    encrypted = cipher.encrypt('Secret Message A')
    decrypted = cipher.decrypt(encrypted)
    print(encrypted)
    print(decrypted)
"""


