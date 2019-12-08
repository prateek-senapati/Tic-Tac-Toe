# COURSE: Complete Python Bootcamp: Go from zero to hero in Python 3
# INSTRUCTOR: Jose Portilla
# PLATFORM: Udemy

# Milestone Project - 1: TIC-TAC-TOE

# Function to display the updated game board
def print_grid(grid_list):
    print("\n")
    print(f"{grid_list[6]} | {grid_list[7]} | {grid_list[8]}")
    print("-- --- --")
    print(f"{grid_list[3]} | {grid_list[4]} | {grid_list[5]}")
    print("-- --- --")
    print(f"{grid_list[0]} | {grid_list[1]} | {grid_list[2]}")
    print("\n")

# Function to check if the given player has won the game or not
def check_win(grid_list, marker):
    return  grid_list[6] == grid_list[7] == grid_list[8] == marker or \
            grid_list[3] == grid_list[4] == grid_list[5] == marker or \
            grid_list[0] == grid_list[1] == grid_list[2] == marker or \
            grid_list[6] == grid_list[3] == grid_list[0] == marker or \
            grid_list[7] == grid_list[4] == grid_list[1] == marker or \
            grid_list[8] == grid_list[5] == grid_list[2] == marker or \
            grid_list[6] == grid_list[4] == grid_list[2] == marker or \
            grid_list[8] == grid_list[4] == grid_list[0] == marker

# Function to check if the game board is full or not
def grid_complete(grid_list):
    return ' ' not in grid_list

# Function to take a valid grid position input from the given player
def get_valid_position(grid_list, player):
    valid_position_found = False
    valid_positions = [str(x) for x in range(1, 10)]
    while not valid_position_found:
        position = input(f"\n{player}, please enter a valid grid position (1-9): ")
        while position not in valid_positions:
            position = input(f"\n{player}, please enter a valid grid position (1-9): ")
        if grid_list[int(position) - 1] == ' ':
            valid_position_found = True
        else:
            print("\nThis position is already occupied. Please select another position.\n")
    return int(position) - 1

# Function to implement the gameplay
def tic_tac_toe(player1, player2, scores_dict):
    current_grid_list = [' '] * 9
    while True:
        # Player 1 (marker: X)
        position = get_valid_position(current_grid_list, player1)
        current_grid_list[position] = 'X'
        print_grid(current_grid_list)
        if check_win(current_grid_list, 'X'):
            print(f"\nCongratulations {player1}! You have won the game :)\n")
            scores_dict['Player 1'] += 1
            return scores_dict
        if grid_complete(current_grid_list):
            print("\nThe game ended in a draw!!\n")
            scores_dict['Tie'] += 1
            return scores_dict
        #Player 2 (marker: O)
        position = get_valid_position(current_grid_list, player2)
        current_grid_list[position] = 'O'
        print_grid(current_grid_list)
        if check_win(current_grid_list, 'O'):
            print(f"\nCongratulations {player2}! You have won the game :)\n")
            scores_dict['Player 2'] += 1
            return scores_dict

print("\nTIC-TAC-TOE\n")
print("\nINSTRUCTIONS:")
print("\n(1) Player 1's marker is 'X' and Player 2's marker is 'O'.")
print("(2) Player 1 (marker: X) always goes first.")
print("(3) Use the Numpad of your keyboard for best experience.\n")
player1 = input("Enter player 1 (marker: X) name: ")
player2 = input("Enter player 2 (marker: O) name: ")
scores_dict = {'Player 1': 0, 'Tie': 0, 'Player 2': 0}
while True:
    print("\nHere are the grid positions:\n")
    print("7 | 8 | 9")
    print("-- --- --")
    print("4 | 5 | 6")
    print("-- --- --")
    print("1 | 2 | 3")
    print("\n")
    scores_dict = tic_tac_toe(player1, player2, scores_dict)
    print(f"\n{player1}: {scores_dict['Player 1']}\t\tTie: {scores_dict['Tie']}\t\t{player2}: {scores_dict['Player 2']}")
    choice = input("\n\nDo you want to play again? (Enter 'yes' or 'no'): ")
    if choice.lower() == 'yes':
          continue
    else:
          print("\nThanks for playing! :)\n")
          break
