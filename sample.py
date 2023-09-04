import rsa
from modules import keys
from modules import utils

# This is a sample code that shows how to obtain
# PEM keys and how to use them to encrypt and
# decrypt a simple message.
 
# Generate private pem key pair
keys.generate()

# Load Keys
privateKey = keys.loadPrivateKey() 
publicKey = keys.loadPublicKey()

# This is the string that we will be encrypting
message = "Hello World"
 
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = utils.encrypt(message,publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# the encrypted message can be decrypted
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption

decMessage = utils.decrypt(encMessage,privateKey)
print("decrypted string: ", decMessage)
