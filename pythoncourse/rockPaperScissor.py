import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('Do you want rock, paper or scissors? ')

print('The computer chose: ' + computer_choice)

if computer_choice == user_choice:
    print('Tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win!')
else:
    print('You lose!')