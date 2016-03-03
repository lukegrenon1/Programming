import random

comp_choice = random.randint(1,3)
player = input('Please select either "rock", "paper" or "scissors" ')
win = 'You win!'
c_win = 'Computer Wins!'

while (player != 'rock' and player != 'paper' and player != 'scissors'):
    print(player)
    player = input('That is not a valid guess. Please select either "rock", "paper" or "scissors" ')

if (comp_choice == 1):
    comp_choice = 'rock'
elif (comp_choice == 2):
    comp_choice = 'paper'
elif (comp_choice == 3):
    comp_choice = 'scissors'
else:
    print('Error... Error!!')
   
if (player == comp_choice):
    print('Tie!!')
elif (player == 'rock'):
    if (comp_choice == 'paper'):
            print(c_win)
    else:
            print(win)
elif (player == 'paper'):
    if (comp_choice == 'scissors'):
            print(c_win)
    else:
            print(win)
elif (player == 'scissors'):
    if (comp_choice == 'rock'):
            print(c_win)
    else:
            print(win)
        
print("Your choice: " + player + "\nComputer choice: " + comp_choice + "\nThank you for playing!");
input("Enter any key to exit.");        
