from EncryptQR import EncryptQR
test = EncryptQR()
test.encrypt("sensitiveinfo.txt", "badpassword", "aes128")
test.decrypt("test.png", "badpassword", "aes128")