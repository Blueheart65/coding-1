#loop - a loop is a constuct (special function) that repeats itself. 
# in programming, a loop allows you to repeat code intructions.
#while loop - a type of loop where so long as a condition is equal to true, it will keep running 
# the key word is while --> do while 

#synax 
num = 4
while 2+2 == num: #condition --> operations - must be True
    print("the program is running")
    num = int(input("please type in any number but 4  to stop the program"))

#while loops will ALWAYS run unless you change a condition
# we can do this by writiong intructions to manually change it.
# the computor ALWYAS completes their task before moving to the next step.

def guessingGame():
    correctAnswer = 8
    attempts = 0

    print("welcome to the guessing game")
    print ("please type in a number 1 though 10")

    useerGuess = int(input("please type in a number"))
    while userguess != correctAnswer:
        print("sorry, incorrect. guess again")
        attempts+=1
        print(attempts)
        userGuess =int(input("please try another number;"))
    print("congrats! you guess correctly")
guessingGame()