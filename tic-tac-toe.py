from tkinter import *
import random

def next_turn(row,col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            #put player 1 sympol
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                #switch player
                player = player[1]
                Label.config(text=(player[1] + "turn"))

            elif check_winner() == True:   
                Label.config(text=(player[0] + "wins!"))

            elif check_winner() == 'tie':   
                Label.config(text=("Tie, No winner!"))    

        elif player == players[1]:
            #put player 2 sympol
            game_btns[row][col]['text'] = player


def next_turn(row, col):
    global player

    # 1. Check if the cell is empty AND the game is not over
    if game_btns[row][col]['text'] == "" and not check_winner():
        # Set the button text to the current player's symbol
        game_btns[row][col]['text'] = player

        # Check for a winner/tie after the move
        winner_result = check_winner()

        if winner_result is True:
            # Current player wins
            label.config(text=(player + " wins!"))
        elif winner_result == 'tie':
            # It's a tie
            label.config(text=("Tie, No winner!"))
        else:
            # No winner yet, switch players
            # Use players.index() to find the next player
            current_player_index = players.index(player)
            next_player_index = (current_player_index + 1) % len(players)
            player = players[next_player_index]
            label.config(text=(player + " turn"))

def check_winner():
    """Checks for win conditions (horizontal, vertical, diagonal) or a tie."""
    # Check all 3 horizontal win conditions
    for row in range(3):
        # Fix: Check for matching symbols AND ensure it's not an empty string
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            # Highlight the winning row and return True
            game_btns[row][0].config(bg="cyan")
            game_btns[row][1].config(bg="cyan")
            game_btns[row][2].config(bg="cyan")
            return True

    # Check all 3 vertical win conditions
    for col in range(3):
        # Fix: Check for matching symbols AND ensure it's not an empty string
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "": # Added missing ['text']
            # Highlight the winning column and return True
            game_btns[0][col].config(bg="cyan")
            game_btns[1][col].config(bg="cyan")
            game_btns[2][col].config(bg="cyan")
            return True

    # Check diagonals conditions
    # Top-left to bottom-right
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True
    # Top-right to bottom-left
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # Check for a tie (if no winner and no empty spaces)
    if not check_empty_spaces():
        # Highlight all buttons in case of a tie
        for row in range(3):
             for col in range(3):
                  game_btns[row][col].config(bg='red')
        return 'tie'

    # If no win and spaces are left
    return False

def check_empty_spaces():
    """Checks if there are any empty cells left on the board."""
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] == "":
                return True # Found an empty space

    return False # No empty spaces left (board is full)

def start_new_game():
    """Resets the board and starts a new game."""
    global player
    # 1. Randomly select the starting player
    player = random.choice(players)

    # 2. Update the label to show whose turn it is
    label.config(text=(player + " turn")) # Fix: Used 'label' not 'Label.config'

    # 3. Reset all buttons
    default_bg = game_btns[0][0].cget("background") # Get Tkinter's default button color
    for row in range(3):
        for col in range(3):
            # Fix: Use .config() method and reset both text and background
            game_btns[row][col].config(text="", bg=default_bg) # Use default_bg or a specific color like 'lightgray'

# --- Initialization ---

window = Tk()
window.title("Tic-Tac-Toe")

# Define players and choose the starting player
players = ["X", "O"] # Capitalized for better visibility
player = random.choice(players) # Will hold the current player's symbol

# Game button storage (list of lists)
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Label to display game status (Turn, Win, Tie)
# Fix: Renamed the variable to lowercase 'label' to avoid conflict with the Tkinter class 'Label'
label = Label(text=(player + " turn"), font=('consolas', 40)) # Fix: Changed 'true' to 'turn'
label.pack(side="top")

# Restart button
restart_btn = Button(text="Restart", font=(
    'consolas', 20), command=start_new_game)
restart_btn.pack(side="top")

# Frame to hold the 3x3 grid of buttons
btns_frame = Frame(window)
btns_frame.pack()

# Create the 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                                    command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()