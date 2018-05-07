class EncryptQR:
	def __init__(self): 
		self.maxSizeBytes = 2956

	def generateAES(self, key, blockSize):
		from AES import AES
		bytesBS = int(blockSize[3:])/8
		return AES(key, int(bytesBS))

	def encrypt(self, path, key, blockSize): 
		encryptedData = None
		with open(path, "rb") as binary_file:
			bytesData = binary_file.read()
			aes = self.generateAES(key, blockSize)
			encryptedData = aes.encrypt(str(bytesData))
		binary_file.close()

		lenData = len(encryptedData)
		diff = str(abs(lenData-self.maxSizeBytes))
		if (lenData > self.maxSizeBytes):
			print("You are exceeding the Max QR Size By: "  + diff + " Bytes")
		else:
			import pyqrcode
			print("You have " + diff + " Bytes remaining")
			print("Generating Encrypted QR Code PNG...")
			qr = pyqrcode.create(encryptedData, error='L', version=40, mode='binary')
			#TODO: ENCRYPT PATH NAME (TEST IS TEMPORARY)
			import png
			qr.png('test.png')

	def decrypt(self, path, key, blockSize):
		from PIL import Image
		import zbarlight
		
		decodedData = None
		with open(path, 'rb') as image_file:
			image = Image.open(image_file)
			image.load()
			decodedData = zbarlight.scan_codes('qrcode', image)[0]
		image_file.close()

		with open('test.txt', "wb") as binary_file:
			aes = self.generateAES(key, blockSize)
			decryptedData = aes.decrypt(decodedData)
			binary_file.write(decryptedData)
		binary_file.close()
			    