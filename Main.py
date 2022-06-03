import random

player = int(input("Do you want to play a game: 1 (YES), 2 (NO): \n"))
if player == 1:
    print("You are welcome")
elif player == 2:
    print("Have a nice day")
else:
    print("You entered an invalid option")    
        

while True:
    user_move = input("Enter your choice: (rock, paper, scissors): ")
    valid_move = ["rock", "paper", "scissors"]
    computer_move = random.choice(valid_move)
    print(f"\nYou chose {user_move}, computer chose {computer_move}.\n")

    if user_move == "rock" and computer_move == "rock":
        print("it\"s a draw!")
    elif user_move == "rock" and computer_move == "paper":
        print("user lost!")
    elif user_move == "rock" and computer_move == "scissors":
        print("user wins!")
    elif user_move == "paper" and computer_move == "rock":
        print("user wins!")
    elif user_move == "paper" and computer_move == "paper":
        print("it\"s a draw!")
    elif user_move == "paper" and computer_move == "scissors":
        print("user lost!")
    elif user_move == "scissors" and computer_move == "rock":
        print("user lost!")
    elif user_move == "scissors" and computer_move == "paper":
        print("user wins!")
    elif user_move == "scissors" and computer_move == "scissors":
        print("it\"s a draw!")
    else:
        print("wrong option selected")
    
    exit = input("Do you still want to play? (y/n) \n")
    if  exit.lower() != 'y':
        break
    
                
            
                     
