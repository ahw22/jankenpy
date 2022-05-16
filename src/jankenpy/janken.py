# Simple janken terminal game
import random

from jankenpy.io.InputControllerTUI import TUIInputController
from jankenpy.io.IOController import IOController
from jankenpy.io.OutputControllerTUIPrinter import TUIPrinter


def start_game(iocontroller: IOController):
    iocontroller.outputcontroller("Welcome to a very simple Janken game!")
    iocontroller.outputcontroller("What is your name?\n")
    playerName = iocontroller.inputcontroller.get_str()
    iocontroller.outputcontroller(f"Hello {playerName}")
    return playerName


def play_round(playerName, iocontroller: IOController):
    """Plays a round of janken

    Args:
        playerName (str): player Name

    Returns:
        int: 0 = Draw, 1 = Player 1 won, 2 = CPU(Player 2) won
    """
    cpuChoice = random.randrange(0, 3)  # TODO
    playerChoice = get_player_choice(iocontroller)

    # check choices
    if cpuChoice not in range(3):  # TODO
        raise ValueError(f"CPU chose an invalid number! Got: {cpuChoice}")
    if playerChoice not in range(3):  # TODO
        raise ValueError(f"{playerName} chose an invalid number! Got: {playerChoice}")

    result = who_won(playerChoice, cpuChoice, playerName, iocontroller)
    return result


def get_player_choice(iocontroller: IOController):
    playerChoice = None
    while playerChoice is None:
        iocontroller.outputcontroller("Pick a card to play.")
        iocontroller.outputcontroller("Rock = 0, Paper = 1, Scissors = 2")
        try:
            iocontroller.outputcontroller("To pick a card press a number from 0 to 2\n")
            playerChoice = int(iocontroller.inputcontroller.get_int(validator=lambda x: x in range(3)))

        except ValueError as e:
            iocontroller.outputcontroller(
                f"Number too large, try again! {e}"
            )
            playerChoice = None
            continue

    return playerChoice


def who_won(playerChoice, cpuChoice, playerName, iocontroller: IOController):
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
    iocontroller.outputcontroller(f"\n{playerName} chose: {choices[playerChoice]}")
    iocontroller.outputcontroller(f"The computer chose: {choices[cpuChoice]}")
    result = (len(choices) + playerChoice - cpuChoice) % 3
    return result


def main():
    iocontroller = IOController(TUIInputController(), TUIPrinter())
    rounds = 3
    roundsPlayed = 0
    player1Score = 0
    player2Score = 0
    playerName = start_game(iocontroller)
    while roundsPlayed < rounds:
        iocontroller.outputcontroller(f"\n\n\nRound {roundsPlayed + 1}")
        winner = play_round(playerName, iocontroller)
        if winner == 0:
            rounds += 1  # we need to play an extra round
            iocontroller.outputcontroller("It's a draw! Play again!")
        elif winner == 1:
            player1Score += 1
            iocontroller.outputcontroller(f"{playerName} won!")
        elif winner == 2:
            player2Score += 1
            iocontroller.outputcontroller("The computer won!")

        roundsPlayed += 1
        iocontroller.outputcontroller("The score is:")
        iocontroller.outputcontroller(f"{playerName} has {player1Score} points!")
        iocontroller.outputcontroller(f"The computer has {player2Score} points!")


if __name__ == "__main__":
    main()
