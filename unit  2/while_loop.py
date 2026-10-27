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
    print("would you like another Y/N?")

def BBqchips():
    print("here are your BBq chips")
    print("would you like another Y/N?")

def  PlainChips():
    print("here are your Plain chips")
    print("would you like another Y/N?")

def water():
    print("here is your water")
    print("would you like another Y/N?")

def Coke():
    print("here is your coke") 
    print("would you like another Y/N?")



vendingMachine = str(input("welcome to the vending machine"))
while vendingMachine != "N":
 if vendingMachine == "B2":
    print ("You have chosen nachos")
    Nachos()
 elif vendingMachine == "G2":
    print("you have chosen BBQ Chips")
    BBqchips()
 elif vendingMachine == "B7":
    print("you have chosen plain chips")
    PlainChips()
 elif vendingMachine == "G7":
    print("you have chosen water")
    water()
 elif vendingMachine == "B3":
    print("you have chosen Coke")
    Coke()
 else:
    print("function not avaiable")


# import random
# selection = input("would you like to roll or quit r/q")
# r = 1
# q = 2
# if selection == 1:
#      print(random.randint(1, 7))
# elif selection == 2:
#     print("you have quit the game")
# else:
#     print("not defined")


# def play():
#     choice = 1
#     attempts = 3

# # i dont have much becuase I had to run a bunch of test to test how this "randint" thing worked
# and everytime i used it it kept say a word was not defined but i tried all period and im stil having trouble
# but i just know you CANNOT do random words only random numbers, even if you assign the word to a number