print('Hello, welcome to my computer quiz! ')
#player is asked if they want to play the game
playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()
else:
    print('Okay! Let us play')
# this is to show that the score at this moment is 0
score = 0

# a variable is placed with the question, and if the answer is correct then 'you are correct' is printed
answer = input('what does CPU stand for? ')
if answer == 'central processing unit':
    print('you are correct!')
# if the answer is correct then one point is added to the score
    score += 1
else:
    print('incorrect!')

answer = input('What does GPU stand for? ')
if answer == 'graphic processing unit':
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input('What does RAM stand for? ')
if answer == 'random access memory':
    print('correct')
    score += 1
else:
    print('incorrect')

print('you got ' + str(score) + ' questions correct! ')