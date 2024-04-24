'''
Author: Stavri Gkousi
email: 20220338@student.act.edu
copyrihght 20220338
Note: the reason it seems like overkill is because i wanted to test myself
in this new areas i learned
'''
import string as str

x=str.ascii_lowercase # temporary place to hold ascii lowercase characters
y=[]   # make array to hold each character of alphabet
for char in x:
    y.append(char)  # puts a character of the alphabet as a single place holder in the array

alphabet={} # create dictionary to hold the normal text and encrypted one
count=0
for i in y:
    if count<23:
      alphabet[y[count]]=y[count+3]
      count+=1
    else:
        alphabet[y[count]]=y[count-23]
        count += 1
def encrypt(target):  # create the method for encrypting
     text=[]
     for char in target:
         text.append(char.lower()) # from the string gets only the characters in a string and puts it in the list
     encrypted=[] # creates the list that has the encrypted letters
     keys=list(alphabet.keys())

     count=0
     for i in text:
         for j in keys:
             x=keys[count]
             if i==x:
                 encrypted.append(alphabet[keys[count]]) # the encrypted letters are put into the list
                 count = 0
                 break;
             else:
               count+=1


     return encrypted


def decrypt(target):  # create the method for encrypting
    text = []
    for char in target:
        text.append(char.lower())
    encrypted = []
    keys=list(alphabet.keys())


    count = 0
    for i in text:
        for j in keys:
            x = alphabet[keys[count]]
            if i == x:
                encrypted.append(keys[count])
                count = 0
                break;
            else:
                count += 1

    return encrypted

text=input("Enter your text for encryption: \n")

print(answer:= encrypt(text),end=" ")
text=input("Enter your text for decryption: \n")
print(answer:= decrypt(text),end=" ")


gi