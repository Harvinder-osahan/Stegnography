import cv2
import string
import getpass as gp 

enc = {} 
dec = {} 

for i in range(255):
    enc[chr(i)] = i
    dec[i] = chr(i)

pic = cv2.imread("pic.jpg")

i = pic.shape[0]
j = pic.shape[0]

key = gp.getpass("Enter the Secret Key:" )
text = gp.getpass("Enter the text to encrypt: ")

kl = 0

z=0; x=0; y=0

l = len(text)

#Encryption, the code will hide data in top left corer

for i in range (l):
    pic[x, y, z] = enc[text[i]] ^ enc[key[kl]]
    x = x+1
    y = y+1
    z = (x+1) % 3 
    kl = (kl+1) % len(key)

cv2.imwrite("e_pic.jpg", pic)
b = cv2.imread("e_pic.jpg")
cv2.imshow("encrypted_image", b)
print("!Data hidden successfully!")
