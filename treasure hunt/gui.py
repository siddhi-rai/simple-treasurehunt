import tkinter as tk
from game_logic import Game

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Treasure Hunt")
        self.game = Game()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=500, height=500, borderwidth=0, highlightthickness=0, bg="lightgray")
        self.canvas.pack()
        self.draw_map()

        self.master.bind("<Up>", lambda event: self.move_player("up"))
        self.master.bind("<Down>", lambda event: self.move_player("down"))
        self.master.bind("<Left>", lambda event: self.move_player("left"))
        self.master.bind("<Right>", lambda event: self.move_player("right"))

    def draw_map(self):
        self.canvas.delete("all")
        cell_width = 500 / self.game.map_size
        for i in range(self.game.map_size):
            for j in range(self.game.map_size):
                color = "gray" if (i + j) % 2 == 0 else "lightgray"
                self.canvas.create_rectangle(i*cell_width, j*cell_width, (i+1)*cell_width, (j+1)*cell_width,
                                             fill=color, outline="black")
        self.draw_treasures()
        self.draw_player()

    def draw_player(self):
        cell_width = 500 / self.game.map_size
        x0 = self.game.player_position[0] * cell_width + cell_width * 0.2
        y0 = self.game.player_position[1] * cell_width + cell_width * 0.2
        x1 = x0 + cell_width * 0.6
        y1 = y0 + cell_width * 0.6
        self.player = self.canvas.create_oval(x0, y0, x1, y1, fill="blue")

    def draw_treasures(self):
        cell_width = 500 / self.game.map_size
        for treasure_position in self.game.treasure_positions:
            x0 = treasure_position[0] * cell_width + cell_width * 0.2
            y0 = treasure_position[1] * cell_width + cell_width * 0.2
            x1 = x0 + cell_width * 0.6
            y1 = y0 + cell_width * 0.6
            self.canvas.create_oval(x0, y0, x1, y1, fill="gold", outline="black")

    def move_player(self, direction):
        self.game.move_player(direction)
        self.draw_map()

def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
