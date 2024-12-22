# generate a random number 
# Loop
    # ask the user to make a guess 
    # If not a valid number
    #  print an errror
    # If number < guess 
    #  print too low 
    # If number > guess 
    #  print too high 
    # Else 
    # print well done
import random 

number_to_guess = random.randint(1,100)
while True:
    try: 
        guess = int(input('Guess the number between 1 and 100: '))
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')

