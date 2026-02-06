'''Hot Dog Program
By Grace LeVoir
2 - 5 - 2026'''


# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

cost = 0.0

#Ask about hot dog or chili dog
hot_dog = input('Do you want a hot dog? (y/n): ')
if hot_dog == 'y':
        cost = 3.50
if hot_dog == 'n':
    chili_dog = input('Do you want a chili dog? (y/n): ')
    if chili_dog == 'y':
        cost = 4.50
    if chili_dog == 'n':
        print('No more hot dog options.')


#Ask about cheese
cheese = input('Do you want cheese? (y/n): ')
if cheese == 'y':
    cost2 = cost + 0.50
if cheese == 'n':
    cost2 = cost


#Ask about peppers
peppers = input('Do you want peppers? (y/n): ')
if peppers == 'y':
    cost3 = cost2 + 0.75
if peppers == 'n':
    cost3 = cost2


#Ask about grilled onions
grilled_onions = input('Do you want grilled onions? (y/n): ')
if grilled_onions == 'y':
    cost4 = cost3 + 1.00
if grilled_onions == 'n':
    cost4 = cost3


#Calculate the tax
tax = cost4 * 0.07

#Calculate the total
total = cost4 + tax

#Display cost, tax, and total
print(f'Your cost is: ${cost4:0.2f}')
print(f'Your tax is: ${tax:0.2f}')
print(f'Your total is: ${total:0.2f}')