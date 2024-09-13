from PIL import Image
import numpy as np
def encrypt():
    path=input("Enter the Path of image: ")
    print("Provide a numeric value of key to encrypt the image & remember it to decrypt the image")
    print("Values should be between 0 & 255")
    shift = [int(input("Enter first value: ")), int(input("Enter second value: ")), int(input("Enter third value: "))]
    image = Image.open(path)
    imgArray = np.array(image)
    key = np.resize(shift, imgArray.shape)
    key = key.astype(np.uint8)
    # print(key)
    encryptedArray = np.bitwise_xor(imgArray, key)
    # print(encryptedArray)
    encryptedImg = Image.fromarray(encryptedArray)
    encryptedImg.save("encrypt.png")
    print("Image encrypted successfully.")

def decrypt():
    path=input("Enter the Path of image: ")
    print("Values should be between 0 & 255")
    print("Provide a numeric value of key to decrypt the image & make sure it is same as that used at the time of encryption")
    shift = [int(input("Enter first value: ")), int(input("Enter second value: ")), int(input("Enter third value: "))]
    image = Image.open(path)
    imgArray = np.array(image)
    key = np.resize(shift, imgArray.shape)
    key = key.astype(np.uint8)
    decryptedArray = np.bitwise_xor(imgArray, key)
    decryptedImg = Image.fromarray(decryptedArray)
    decryptedImg.save("decrypt.png")
    print("Image decrypted successfully.")    



End = False
while not End:
    print("Choose from the following:")
    print("1. Encrypt \n2. Decrypt")
    choice = int(input("What do you want to do:"))
    if choice==1:
        encrypt()
    elif choice ==2:
        decrypt()
    else:
        print("Choose Between 1 and 2 only")
    con=int(input("Do you want to continue \n1. Yes \n2. No \n"))
    if con == 2:
        End = True

