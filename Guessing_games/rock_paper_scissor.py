# Ask the user to make a choice 
# If choice is not valid 
#   Print an error 
# Let the computer to make a choice 
# Print choices (emojis)
# Determine the winner 
# Ask the user if they want to continue 
# If not 
#   terminate 
import random # to make computer make a choice import random module 

choices = ('r','p','s') # we want to make this tuple instead of list so that it cannot be changed
user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower() # store a value for making variable and asking it to be lower
if user_choice not in choices:
    print('Invalid choice!')
computer_choice = random.choice(choices)


# refactoring code 
# modularization 
