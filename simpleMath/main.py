#  ---------------------------------------------
#  | Description: This program shows how to use|
#  | for loops, range, and getting the product |
#  | and sum of a list through an if statement |
#  |                                           |
#  | Created by: Edreih Aldana                 |
#  ---------------------------------------------

aList = []  # The first list that will hold the numbers less than 25 which are to be multiplied together
bList = []  # The second list that will hold the numbers greater than or equal to 25 which will be added together
product = 1

print("""This program will ask you to input 5 numbers. Out of those numbers
    the ones that are less than 25 will be multiplied together. The numbers
    that are greater than or equal to 25 will be added together.""")

for x in range(0, 5):
    number = int(input("Enter a number:\n"))
    if number < 25:
        aList.append(number)
    if number >= 25:
        bList.append(number)

print("The product of the numbers less than 25 are:")
for n in aList:
    product *= n
print(product)

print("The sum of the numbers greater than or equal to 25 that were entered are:")
print(sum(bList))