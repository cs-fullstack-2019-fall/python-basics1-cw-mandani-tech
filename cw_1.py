
# ### Problem 1:
# Create two variables. One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.

stringVar1 = ("My name is:")
stringVar2 = ("Hamida")
print(stringVar1 + stringVar2)


# ### Problem 2:
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.
#

extraCredit= int(input("Enter the extra credit:"))
if(extraCredit <5):
    print("That’s not enough extra credit.")
elif(extraCredit>20):
    print("That’s too much extra credit.")

# ### Problem 3:
# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.
#
usrPassWord= input("Enter a password here: ")
checkPassword=input("What is the password:")
if (usrPassWord == checkPassword):
    print("You got it")
else :
    print("Wrong Password")


# ### Problem 4:
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”
card1=int(input("Enter your first card number:"))
card2=int(input("Enter your second card number"))
sum= card1 +card2
if (sum==21):
    print("BLACKJACK!")
elif (sum>21):
    print("BUST!")
else :
    print ("The total is " + str(sum))