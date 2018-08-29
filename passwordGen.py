'''
Written by AntiAncheta, the world's Roast God and also Meme Ka-weeeen
Does what a password generator does
Oh and if you type password then it just spams you with roasts so don't do it
'''
import random, os, time

# We define a function for generating the password, takes a password as an argument to see how bad I should roast you
def passGen(password):
    # Define an array of characters, lowercase and uppercase, as well as numbers and special characters
    listStuff = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"!","@","#","$","%","&","(",")",">","<","?","1","2","3","4","5","6","7","8","9","0"]
    # YOU PICKED THE WRONG PASSWORD, FOO
    badPasswords = ["password", "password123", "alohi123", "bradah808", "brah808", "808countrygrindzcuz", "dakine"] # If you really want you can add to this list
    # Now that all of that is listed, we generate a password, check if the argument passed in the function (the password) is in badPassword array and then make our decision
    if password in badPasswords:
        # You picked the wrong house foo
        while True:
            print("BRO YOU ARE TRASH STOP IT BRO GO HOME AND THINK ABOUT THIS BRO\n")
    else:
        # Woo make a new password from random choices in the array
        newPass = random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff) + random.choice(listStuff)
        # Print it
        print("Your new password is: " + newPass +"\n")

# We define a variable that stores user input, their password. We DO NOT save, store, or do anything else with their password besides compare it to a password in the badPasswords list.
theirPass = input("Your Password: ")
passGen(theirPass)
    
