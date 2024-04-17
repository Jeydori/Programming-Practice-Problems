#Repititive Problem 
import random

ranNum = random.randint(1, 101)
guess = int(input('Guess the number from 1-100: '))

if guess < 1 or guess > 100:
    print("Please enter a number between 1 and 100.")
elif ranNum == guess:
    print('You got the correct number!!!')
    print('\n Random number is', ranNum, 'and you guessed it right')
elif ranNum > guess:
    print('The random number is greater than your guessed number')
    print('Random Numer:', ranNum, '|', 'Guessed Number', guess)
elif ranNum < guess:
    print('The random number is less than your guessed number')
    print('Random Numer:', ranNum, '|', 'Guessed Number', guess)
