import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

winCounter = 0
drawCounter = 0
loseCounter = 0

while(True):
    player_move = input("Choose [r]ock,[p]aper or [s]cissors: ")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move == paper
    elif player_move == 's':
        player_move == scissors
    else:
        raise SystemExit('Invalid input. Try again...')
            
    computer_move = ""
    computer_random_move_number = random.randint(1,3)
    
    if computer_random_move_number == 1:
        computer_move = paper
    elif computer_random_move_number == 2:
        computer_move = scissors
    else:
        computer_move = rock
    if(player_move == rock and computer_move == scissors or player_move == scissors and computer_move == paper or player_move == paper and computer_move == rock):
        print("Congratulations!You win!")
        winCounter += 1

    elif(player_move == computer_move):
        print('Draw')
        drawCounter += 1

    else:
        print("You lost!")
        loseCounter += 1
    
    print("Do you want another game? [y]es or [n]o")
    answer = input()
    if(answer == 'y'):
        continue
    elif(answer == 'n'):
        break
    else:
        break
    
    
print(f"Wins: {winCounter} | Draws: {drawCounter} | Losts: {loseCounter}")
