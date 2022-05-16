# Simple janken terminal game
import random



cards = ["Scissors", "Paper", "Rock"]
def start_game():
    print("Welcome to a very simple Janken game!")
    playerName = input("What is your name?\n")
    print("Hello " + playerName)
    return

def play_round():
    cpu_choice = -1
    cpu_choice = random.randrange(0,3)
    if (cpu_choice == -1):
        print("No random number")
    elif(cpu_choice > 2):
        print("Number too big")
    get_player_choice()
    print(cpu_choice)
    
    
def get_player_choice():
    playerChoice = -1
    while(playerChoice == -1):
        print("Pick a card to play.")
        print("Scissors = 0, Paper = 1, Rock = 2")
        try:
            playerChoice = int(input("To pick a card press a number from 0 to 2\n"))
        except ValueError:
            print("Invalid Input, try again!")
            playerChoice = -1
        except (playerChoice < 2):
            print("Number too large, try again!")
            playerChoice = -1
        

def main():
    start_game()
    rounds = 3
    for counter in range(rounds):
        print("Round " + str(counter + 1))
        play_round()

   
        
    
  






if __name__=="__main__":
    main()