import rsa

def encrypt(message,publicKey):
    return rsa.encrypt(message.encode(),
                         publicKey)

def decrypt(message,privateKey):
    return rsa.decrypt(message, privateKey).decode()