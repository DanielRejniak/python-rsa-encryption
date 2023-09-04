import rsa

def encryptText(message,publicKey):
    return rsa.encrypt(message.encode(),
                         publicKey)

def decryptText(message,privateKey):
    return rsa.decrypt(message, privateKey).decode()