#what is a loop--> code that repeats
# WHile loops = a block code that repeats itself until the triggering condition is no longer True. Can be infinate 
# for loops = a type of loop ( code block that re[eats itse;f ) But it only repeats itself upto a certain number of times.
# it is infinate

#Think of for loop as the counting Loop = for --> 4 number of loop
#For loop synax 
# I stand for iterator = programmers decided maked this the universal symbal for a placeholder for counting 


# for i in range (1, 5):
#     print(i)

# for i in"S c h o o l":
#     print(i)


# #list --> A collection type that acts as a container for multiple data types 
# # and peices of data.

# #list syntax 
# # A list is written like a variable but after the equal assaignment symbol we use square brackets and put all of the data inside of them

# fooditem1 = "popcorn" # we can only store ! peice of data in 1 variable
# grocerylist=["popcprn", "apples", "water","chips", "fish", "celery"]
# print(grocerylist)
# for junk in grocerylist:
#     print("i need to buy" + str (grocerylist))

# itemprices= [10.00, 20.00, 13.99, 7.95, 349.00]
# tax = 0.07
# for cost in itemprices:
#     #I want to know how much in taxes I need to pay each Item
#     print(tax*cost)

# semesterGrades = [90,100, 78, 76 , 74, 82, 84]

# for i in semesterGrades:
#     # I want to find all the grades lower than 85
#     if i < 85:
        # print(i)


Calculation = [10, 15, 78, 98, 69, 95]
for oldNum in Calculation:
    newNum = oldNum * 3
    print("old number" + str(oldNum))
    print("New number" + str(newNum))
    if newNum < 120:
        print("This number is less than 120")
    elif  newNum > 120:
         print("This number is good")




#list are collection types for storing multiple peices of data 
#key elements and purposes for lists:
#list are organis=zed and structured 
#list can be manipulated and modified - mutable(means changable)
#list items are accessable and usbale
#when we want access an item in a list we use the indexing system every item 
#in a list is numberd.
# a list index always starts at (0)


inventory =  [ "sword", "sheild","healing potion", "armor"]
print (inventory [0]) # indicated in going to first posistion in the list 

#when you want to add something to our list, we use the append() method

inventory.append("knife")
inventory.append ("warhammer")
inventory.remove("healing potion")
inventory.insert(4, "healing potion")

print(inventory)




