print("Welcome to the game")
import random
def game():  

    player_input=input("Choose from 'Rock', 'Paper' and 'Scissor':")
    computer_input= random.choices(['Rock','Paper','Scissor'])
    print(f"You chose {player_input}  \nComputer chose {computer_input}")

    if player_input==computer_input:
        print("Draw")
    elif player_input=='Rock' and computer_input=='Scissor':
        print("You win")
    elif player_input=='Scissor' and computer_input=='Paper':
        print("You win")
    elif player_input=='Paper' and computer_input=='Rock':
        print("You win")
    else:
        print("You lost the game")
      

game()


print("Thankyou for playing")
    
    


