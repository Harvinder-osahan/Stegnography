import cv2
import string
import getpass as gp
import os
import pickle
import webbrowser as wb
enc = {}
dec = {}

for i in range(255):
    enc[chr(i)] = i
    dec[i] = chr(i)

print("""\nWant Your Picture clicked or Saved Picture? \n1.Camera\n2. For Saved Picture\n """)
op = int(input())

if op == 1:
    cap = cv2.VideoCapture(0)
    st , pic = cap.read()
    cap.release()
else:
pic = cv2.imread("pic.jpg")



i = pic.shape[0]
j = pic.shape[0]

key = gp.getpass("Enter the Secret Key:" )
text = input("Enter the text to encrypt: ")

kl = 0

z=0; x=0; y=0

l = len(text)
epic = pic
#Encryption, the code will hide data in top left corer
for i in range (l):
    epic[x, y, z] = enc[text[i]] ^ enc[key[kl]]
    x = x+1
    y = y+1
    z = (y+1) % 3
    kl = (kl+1) % len(key)


cv2.imwrite("e_pic.jpg", pic)
b = cv2.imread("e_pic.jpg")
cv2.imshow("encrypted_image", b)

pickle_out = open("ef.pickle","wb")
pickle.dump([l, epic, key, enc, dec], pickle_out)
pickle_out.close()

opn = input("Press \n 1 for Email and Press \n 2 for Whatsapp \n 3 to EXIT")
opn = int(opn)

if opn == 1:
    wb.open('https://mail.google.com')
elif op == 2:
    wb.open('https://web.whatsapp.com/')
else:
    print("Data Hidden Successfully")
    exit()
    
print("!Data hidden successfully!")
