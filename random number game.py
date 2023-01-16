import random

# user is asked to input a number, saved in variable top_of_range
Top_Of_Range = input('Type a number: ')

# to convert the str into int
if Top_Of_Range.isdigit():
    Top_Of_Range = int(Top_Of_Range)

if Top_Of_Range <= 0:
    print('Please enter a number greater than zero next time! ')
    quit()

# to generate a random number

random_number = random.randint(0, Top_Of_Range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('type in a number next time: ')
        continue

    if user_guess == random_number:
        print('you got it right')
        break
    else:
        print('you got it wrong')

print('you got in in', guesses, 'guesses')