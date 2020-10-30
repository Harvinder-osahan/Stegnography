import StegnographyEnc as ef
import getpass as gp
kl=0

tln=len(ef.text)

x = 0 
y = 0 
z = 0 

ch = int(input("\nEnter 1 to extract data from Image : "))

if ch == 1:
    key1=gp.getpass("\n\n Enter the key to extract text : ")
    decrypt=""

    if ef.key == key1 :
        for i in range(ef.l):
            decrypt+=ef.dec[ef.pic[x,y,z]^ef.enc[ef.key[kl]]]
            x=x+1
            y=y+1
            z=(x+1)%3
            kl=(kl+1)%len(ef.key)
        print("Here is your text : ",decrypt)
    else:
        print("Sorry! The Key didn't match.")
else:
    print("Thank you. !!EXITING!!.")
