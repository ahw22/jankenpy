# Simple janken terminal game
import random


def start_game():
    print("Welcome to a very simple Janken game!")
    playerName = input("What is your name?\n")
    print("Hello " + playerName)
    return playerName

def play_round(playerName):
    cpuChoice = -1
    cpuChoice = random.randrange(0,3)
    if (cpuChoice == -1):
        print("No random number")
    elif(cpuChoice > 2):
        print("Number too big")
    playerChoice = get_player_choice()
    result = who_won(playerChoice, cpuChoice, playerName)
    
    
    
def get_player_choice():
    playerChoice = -1
    while(playerChoice == -1):
        print("Pick a card to play.")
        print("Rock = 0, Paper = 1, Scissors = 2")
        try:
            playerChoice = int(input("To pick a card press a number from 0 to 2\n"))
        except ValueError:
            print("Invalid Input, try again!")
            playerChoice = -1
        if playerChoice > 2:
            print("Number too large, try again! The number you chose was:" + str(playerChoice))
            playerChoice = -1
    return playerChoice

#
def who_won(playerChoice, cpuChoice, playerName):
    """Calculates who won using this formula:
    winner = (3 + player - cpu) % 3

    Args:
        playerChoice (int): players chosen weapon
        cpuChoice (int): cpus chosen weapon
        playerName (str): player name

    Returns:
        result: 0 = Draw, 1 = Player 1 won, 2 = CPU(Player 2) won
    """
    choices = ["Rock", "Paper", "Scissors"]
    print(playerName + " chose: " + choices[playerChoice])
    print("The computer chose: " + choices[cpuChoice])
    result = (3 + playerChoice - cpuChoice) % 3
    return result
        


def main():
    playerName = start_game()
    rounds = 3
    for counter in range(rounds):
        print("Round " + str(counter + 1))
        play_round(playerName)

   
        

if __name__=="__main__":
    main()