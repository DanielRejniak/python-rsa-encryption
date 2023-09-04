import rsa
from modules import keys
from modules import utils

# Generate private pem key pair
keys.generate()

# Load Keys
privateKey = keys.loadPrivateKey() 
publicKey = keys.loadPublicKey()

# This is the string that we will be encrypting
message = "Hello World"
 
# Encrypt text message
encMessage = utils.encryptText(message,publicKey)
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# Decrypt encrypted message
decMessage = utils.decryptText(encMessage,privateKey)
print("decrypted string: ", decMessage)

# Encrypt file
utils.encryptFile("./test_files/test.txt",publicKey)

# Decrypt File
utils.decryptFile("./test_files/test.txt",privateKey)
