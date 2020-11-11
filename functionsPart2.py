#Check if any number in a list is even
def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False

result = check_even_list([1,2,3])
print(result)

#Return all even numbers in a list
def check_even_list1(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers

print(check_even_list1([1,2,3,4,5,6]))

#Returning Tuples for Unpacking
work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)

print(employee_check(work_hours))

########################################################
from random import shuffle
def shuffle_list(mylist):
    # Take in list, and returned shuffle versioned
    shuffle(mylist)
    
    return mylist

def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        
        # Recall input() returns a string
        guess = input("Pick a number: 0, 1, or 2:  ")
    
    return int(guess)


# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)

check_guess(mixedup_list,guess)
############################################################################################



