import rsa
import os
 
def generate():

    # Check if keys directory exist
    keysDirectoryExist = os.path.exists("keys")

    # If keys directory does not exist create one along with the keys
    if not keysDirectoryExist:

        # Generate keys directory to store keys
        os.makedirs("keys")

        # Generate new 512 bit keys
        publicKey, privateKey = rsa.newkeys(512)

        # Create private key pem
        with open("./keys/private.pem","wb") as privateKeyPem:
            privateKeyPem.write(privateKey.save_pkcs1("PEM"))

        # Create public key pem
        with open("./keys/public.pem","wb") as publicKeyPem:
            publicKeyPem.write(publicKey.save_pkcs1("PEM"))

    else:

        # Check if keys exist
        privateKeyExists = os.path.exists("./keys/private.pem")
        publicKeyExists = os.path.exists("./keys/public.pem")

        # If one of the keys is missing throw an exception
        if not privateKeyExists or not publicKeyExists:
            raise FileNotFoundError

# Obtain private key pem
def loadPrivateKey():
    with open("./keys/private.pem","rb") as privateKeyPem:
        return rsa.PrivateKey.load_pkcs1(privateKeyPem.read())

# Obtain public key pem
def loadPublicKey():
    with open("./keys/public.pem","rb") as publicKeyPem:
        return rsa.PublicKey.load_pkcs1(publicKeyPem.read())