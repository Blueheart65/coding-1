#loop - a loop is a constuct (special function) that repeats itself. 
# in programming, a loop allows you to repeat code intructions.
#while loop - a type of loop where so long as a condition is equal to true, it will keep running 
# the key word is while --> do while 

#synax 
# num = 4
# while 2+2 == num: #condition --> operations - must be True
#     print("the program is running")
#     num = int(input("please type in any number but 4  to stop the program"))

#while loops will ALWAYS run unless you change a condition
# we can do this by writiong intructions to manually change it.
# the computor ALWYAS completes their task before moving to the next step.

def guessingGame():
    correctAnswer = 8
    attempts = 0

    print("welcome to the guessing game")
    print ("please type in a number 1 though 10")

    userGuess = int(input("please type in a number"))
    while userGuess != correctAnswer:
        print("sorry, incorrect. guess again")
        attempts+=1
        print(attempts)
        userGuess =int(input("please try another number;"))
    print("congrats! you guess correctly")

##guessingGame()



def password ():
    correctPassword = "789"
    attempts = 0

    guess = input("password:")
    while guess != correctPassword:

        print("incorrect try again")
        attempts+=1
    guess = correctPassword
    print("you got it")


#password()

def Nachos():
    print("here are your Nachos")
    print("would you like another")



def vendingMachine():
    print("welcome to the vending machine")
Snacks = (input("please select a snack"))
if Snacks == B2:
    print ("You have chosen nachos")
    Nachos()
vendingMachine()