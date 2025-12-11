from tkinter import *
import random

# --- Global Variables ---
user_symbol = "X"     # Player is always X
ai_symbol = "O"       # AI always O
players = ["X", "O"]
player = user_symbol  # player starts as X
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# ===============================
#         AI MOVE FUNCTION
# ===============================
def ai_move():
    global player

    if player == ai_symbol and not check_winner():
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if game_btns[r][c]['text'] == "":
                    empty_cells.append((r, c))

        if empty_cells:
            row, col = random.choice(empty_cells)
            next_turn(row, col)


# ===============================
#        PLAYER / AI TURN
# ===============================
def next_turn(row, col):
    global player

    if game_btns[row][col]['text'] == "" and not check_winner():

        game_btns[row][col]['text'] = player
        winner_result = check_winner()

        if winner_result is True:
            label.config(text=(player + " wins!"))
        elif winner_result == 'tie':
            label.config(text="Tie, No Winner!")
        else:
            # Switch turn
            player = ai_symbol if player == user_symbol else user_symbol
            label.config(text=(player + " turn"))

            # If AI's turn → play automatically
            if player == ai_symbol:
                window.after(500, ai_move)


# ===============================
#        CHECK FOR WINNER
# ===============================
def check_winner():
    # Horizontal
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            for c in range(3): game_btns[row][c].config(bg="cyan")
            return True

    # Vertical
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            for r in range(3): game_btns[r][col].config(bg="cyan")
            return True

    # Diagonals
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True

    if game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # Tie
    if not check_empty_spaces():
        for r in range(3):
            for c in range(3):
                game_btns[r][c].config(bg="red")
        return 'tie'

    return False


# ===============================
#      EMPTY SPACES CHECK
# ===============================
def check_empty_spaces():
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] == "":
                return True
    return False


# ===============================
#         RESTART GAME
# ===============================
def start_new_game():
    global player
    player = user_symbol  # Player always starts (X)

    default_bg = game_btns[0][0].cget("background")

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg=default_bg)

    label.config(text=(player + " turn"))


# ===============================
#           GUI SETUP
# ===============================

window = Tk()
window.title("Tic-Tac-Toe AI")

label = Label(window, text=(player + " turn"), font=('consolas', 40))
label.pack(side="top")

restart_btn = Button(window, text="Restart", font=('consolas', 20), command=start_new_game)
restart_btn.pack(side="top", pady=5)

btns_frame = Frame(window)
btns_frame.pack()

# Create 3x3 grid
for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(
            btns_frame,
            text="",
            font=('consolas', 50),
            width=4,
            height=1,
            command=lambda r=row, c=col: next_turn(r, c) if player == user_symbol else None
        )
        game_btns[row][col].grid(row=row, column=col)

start_new_game()
window.mainloop()