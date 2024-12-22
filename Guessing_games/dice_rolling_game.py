# loop
    # Ask the user: roll the dice? 
    # If user enters y 
    #   generate two random numbers 
    #   Print them 
    #If user enters n 
    #   Print thank you message
    #   Terminate 
    # Else 
    #   Print invalid choice 

import random

playing = True # loop
while playing:
    choice = input('Roll the dice? (y/n): ').lower()# Ask the user: roll the dice?
    if choice == 'y':    # If user enters y 
        die1 = random.randint(1,6) #   generate two random numbers 
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')  #   Print them
    elif choice == 'n': #If user enters n 
        print('Thanks for playing!') #   Print thank you message
        break #   Terminate
    else:  # Else 
        print('Invalid choice!') #   Print invalid choice 


# next task 
# 1. modify the program so the user can specify how many dice they want to roll. 
# 2. Add a feature that keeps track of how many times the user has rolled the dice during the session. 
#    This will require a counter that increments each time the dice are rolled.
     
    
    
     
    
    
