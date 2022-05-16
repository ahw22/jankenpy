# Simple janken terminal game
import random


def start_game():
    print("Welcome to a very simple Janken game!")
    playerName = input("What is your name?\n")
    print(f"Hello {playerName}")
    return playerName


def play_round(playerName):
    """Plays a round of janken

    Args:
        playerName (str): player Name

    Returns:
        int: 0 = Draw, 1 = Player 1 won, 2 = CPU(Player 2) won
    """
    cpuChoice = random.randrange(0, 3)  # TODO
    playerChoice = get_player_choice()

    # check choices
    if cpuChoice not in range(3):  # TODO
        raise ValueError(f"CPU chose an invalid number! Got: {cpuChoice}")
    if playerChoice not in range(3):  # TODO
        raise ValueError(f"{playerName} chose an invalid number! Got: {playerChoice}")

    result = who_won(playerChoice, cpuChoice, playerName)
    return result


def get_player_choice():
    playerChoice = None
    while playerChoice is None:
        print("Pick a card to play.")
        print("Rock = 0, Paper = 1, Scissors = 2")
        try:
            playerChoice = int(input("To pick a card press a number from 0 to 2\n"))
            if playerChoice not in range(3):  # TODO
                print(
                    f"Number too large, try again! The number you chose was: {playerChoice}"
                )
                raise ValueError("Invalid value chosen!")

        except ValueError:
            print("Invalid Input, try again!")
            playerChoice = None
            continue

    return playerChoice


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
    choices = ["Rock", "Paper", "Scissors"]  # TODO
    print(f"\n{playerName} chose: {choices[playerChoice]}")
    print(f"The computer chose: {choices[cpuChoice]}")
    result = (len(choices) + playerChoice - cpuChoice) % 3
    return result


def main():
    rounds = 3
    roundsPlayed = 0
    player1Score = 0
    player2Score = 0
    playerName = start_game()
    while roundsPlayed < rounds:
        print(f"\n\n\nRound {roundsPlayed + 1}")
        winner = play_round(playerName)
        if winner == 0:
            rounds += 1  # we need to play an extra round
            print("It's a draw! Play again!")
        elif winner == 1:
            player1Score += 1
            print(f"{playerName} won!")
        elif winner == 2:
            player2Score += 1
            print("The computer won!")

        roundsPlayed += 1
        print("The score is:")
        print(f"{playerName} has {player1Score} points!")
        print(f"The computer has {player2Score} points!")


if __name__ == "__main__":
    main()
