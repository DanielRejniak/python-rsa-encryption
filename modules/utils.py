import rsa

def encryptText(message,publicKey):
    return rsa.encrypt(message.encode(),
                         publicKey)

def decryptText(message,privateKey):
    return rsa.decrypt(message, privateKey).decode()

def encryptFile(file_path,publicKey):

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_file = rsa.encrypt(file_data,
                         publicKey)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_file)

def decryptFile(file_path,privateKey):

    with open(file_path, "rb") as file:
        file_data = file.read()

    decrypted_file = rsa.decrypt(file_data,
                         privateKey)
    
    with open(file_path, "wb") as file:
        file.write(decrypted_file)