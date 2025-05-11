import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]  # Row match
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]  # Column match
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]  # Diagonal match
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]  # Diagonal match
    return None

def button_click(row, col):
    global is_x_turn
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = "X" if is_x_turn else "O"
        buttons[row][col]["fg"] = "red"
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_game()
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        is_x_turn = not is_x_turn

def reset_game():
    global is_x_turn
    is_x_turn = True
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Initialize Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="black")

# Boolean to track the turn (True for X, False for O)
is_x_turn = True

# Create a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, bg="black",
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        buttons[row][col] = button

# Start the Tkinter main loop
root.mainloop()