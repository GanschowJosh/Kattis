import sys

def play_ninety_nine():
    your_turn = True
    current_number = 0

    while True:
        if your_turn:
            # Your turn to play
            if current_number % 3 == 0:
                # If the current number is divisible by 3, subtract 2 to avoid a multiple of 3
                move = 2
            else:
                # Otherwise, subtract 1
                move = 1
            current_number += move
            print(move)
        else:
            # Read the opponent's move
            move = int(input())
            current_number += move

        # Check if you or your opponent reached 99
        if current_number == 99:
            if your_turn:
                # You win
                sys.exit(0)
            else:
                # Opponent wins
                sys.exit(0)

        your_turn = not your_turn

play_ninety_nine()
