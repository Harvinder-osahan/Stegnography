import pickle
import getpass as gp
import os

pickle_in = open("ef.pickle", "rb")
l, pic, key, enc, dec = pickle.load(pickle_in)

kl=0

tln = l

x = 0
y = 0
z = 0

ch = int(input("\nEnter 1 to extract data from Image : "))

if ch == 1:
    key1=gp.getpass("\n\n Enter the key to extract text : ")
    decrypt=""

    if key == key1 :
        for i in range(tln):
            decrypt+=dec[pic[x,y,z]^enc[key[kl]]]
            x=x+1
            y=y+1
            z=(x+1)%3
            kl=(kl+1)%len(key1)
        file = open('hid.txt', 'w')
        file.write(decrypt)
        file.close()
        print("check the file.")

    else:
        print("Sorry! The Key didn't match.")
else:
    print("Thank you. !!EXITING!!.")
