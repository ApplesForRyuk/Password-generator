#random password Generator

#1 ask the user if he is interested in generating a random password
#2 if he selects Yes option, the next needed step is to ask for the password's desired length
#3 the password is generated and printed on the screen
#4 else if the initial response is Not at the moment! then exit the programm

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_[]+=><")

def generatePassword():
    passwordLength = int(input("How long would you like you like your password to be?"))
    random.shuffle(characters)
    password = []

    for x in range(passwordLength):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

firstStep = input("Do you want to generate a password? (Yes/No): ")

if(firstStep=="Yes"):
    generatePassword()
elif(firstStep=="No"):
    print("Exiting generator")
    quit()
else:
    print("Something went wrong, please answer again!")
    quit()



