def get_choice(player_name):
    choices = ["Rock", "Paper", "Scissors"]
    choice = input(f"{player_name}, please choose Rock (1), Paper (2), or Scissors (3): ").strip()
    
    while choice not in ["1", "2", "3"]:
        print("INVALID: please choose Rock (1), Paper (2), or Scissors (3)!")
        choice = input(f"{player_name}, please choose Rock (1), Paper (2), or Scissors (3): ").strip()

    return choices[int(choice) - 1]

def display_menu(*items):
    """
    Display the menu items and return the chosen option.
    Takes one tuple object as its argument.
    """
    options = [str(option) for option in range(1, len(items) + 1)]
    selected = ""
    while selected not in options:
        print("\n============== Menu ===============")
        for index, option in enumerate(items):
            print(f"{index + 1}. {option}")
        print("======================================")
        selected = input("Select Option: ")
    return int(selected)

def play_game(player1wins, player2wins, ties):
    global player1_name, player2_name

    # Get player names only if they haven't been set yet
    if not player1_name or not player2_name:
        player1_name = input("What is your name, Player 1? ").strip().capitalize()    
        player2_name = input("What is your name, Player 2? ").strip().capitalize()

    while True:
        # Get choices from both players
        player1_choice = get_choice(player1_name)
        player2_choice = get_choice(player2_name)

        # Display the choices
        print(f"{player1_name} chose: {player1_choice}")
        print(f"{player2_name} chose: {player2_choice}")

        # Determine the result
        if player1_choice == player2_choice:
            result = "It's a tie!"
            ties.append("tie")
        elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
             (player1_choice == "Paper" and player2_choice == "Rock") or \
             (player1_choice == "Scissors" and player2_choice == "Paper"):
            result = f"{player1_name} wins!"
            player1wins.append("win")
        else:
            result = f"{player2_name} wins!"
            player2wins.append("win")

        # Display the result
        print(result)

        # Ask if players want to play again
        again = input("Do you want to play again (y/n)? ").strip().lower()
        if again != "y":
            break

# Global variables to track wins, ties, and player names
player1wins = []
player2wins = []
ties = []
player1_name = ""
player2_name = ""

# Main program loop
while True:
    option = display_menu(
        "Play Rock, Paper, Scissors",
        "View Final Game Report",
        "Exit"
    )
    
    if option == 1:
        play_game(player1wins, player2wins, ties)
    elif option == 2:
        # Display the final game report
        print("\nFinal Game Report:")
        if player1_name and player2_name:
            print(f"{player1_name} wins: {len(player1wins)}")
            print(f"{player2_name} wins: {len(player2wins)}")
            print(f"Ties: {len(ties)}")
        else:
            print("No games have been played yet.")
    elif option == 3:
        # Display the final game report before exiting
        print("\nFinal Game Report:")
        if player1_name and player2_name:
            print(f"{player1_name} wins: {len(player1wins)}")
            print(f"{player2_name} wins: {len(player2wins)}")
            print(f"Ties: {len(ties)}")
        else:
            print("No games have been played yet.")
        
        print("Exiting the program.")

        # Reset all the data for a fresh start
        player1wins.clear()
        player2wins.clear()
        ties.clear()
        player1_name = ""
        player2_name = ""
        break


# Run the game
play_game()




