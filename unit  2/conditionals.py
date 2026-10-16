# conditional If/else logic- these are keywords that intruct your program to do specific
# intructions based on specific data or conditions

# conditional synax 
# bill_amount = int (input("please type in bill tender(1's 5's 10's):"))

# # if usually indicatyws that something is a possible option

# if bill_amount==1:
#  print ("here are 4 quaters")

# #elif allows us to indicate that there are more possible optioms 
# #you can have as many as you want 

# elif bill_amount == 5:
#  print("here are 20 quaters")
# elif bill_amount ==10:
#  print("here are 40 quaters")
# elif bill_amount == 20:
#  print("sorry we dont accept 20s")
# #else is always your last option
# else:
#  print("sorry that type of bill is not accepted")

# def college():
#  grape = int (input("please type here"))
#  if grade > 90:
#    templeU()
#  else:
#   ccp()

# def temple():
#  print("congrats you meet the requiement for temple U")
#  print("2393853")
# def ccp():
#  print("your not accepeted...not to quote mean gilrs but'she doesnt even go here'")



def Calcluate_add():
 n1 = int(input())
 n2 = int(input())
 print(n1 + n2 )
 print ("thank you")
# Calcluate_add()

def Calculate_subtract():
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
    print("thank you...bye")
 #Calculate_subtract()

def Calculate_multiply():
    n1 = int(input())
    n2 = int(input())
    print(n1 * n2)
    print ("your done leave...bye")

#Calculate_multiply()
def Calculate_divide():
    n1 = int(input())
    n2 = int(input())
    print (n1 / n2)
    print("alrightly bye now")

# Calculate_divide()              

Calculate = int(input("please select a caluculation"))
if Calculate == 1:
  print("you have chosen addition, type the numbers you would like to add")
  Calcluate_add()

elif Calculate == 2:
  print("you have chosen subtraction, type in the numbers you would like to subtract")
  Calculate_subtract()

elif Calculate == 3:
  print("you have chosen multiplication, type in the numbers you would like to multiply")
  Calculate_multiply()

elif Calculate == 4:
  print("you have chosen divison, type in in the numbers you would lime to divid")
  Calculate_divide()
  
else:
  print ("fuction not available")
