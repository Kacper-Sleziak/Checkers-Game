from tkinter import *
from Game import Game

if __name__ == "__main__":
    HEIGHT = 800
    WIDTH = 800
    window = Tk()
    canvas = Canvas(window, height=HEIGHT, width=WIDTH)
    window.geometry(f"{str(HEIGHT)}x{str(WIDTH)}")
    window.title("Checkers")
    icon = PhotoImage(file='chess-board.png')
    window.iconphoto(True, icon)

    game = Game(window, canvas)
    game.mainLoop()

    window.mainloop()






#print(board.getMatrix())

# redPawnList = PawnList("red", 30, canvas, window)
# bluePawnList = PawnList("blue", 30, canvas, window)