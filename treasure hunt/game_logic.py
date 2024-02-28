import random
from tkinter import messagebox

class Game:
    def __init__(self, map_size=10, treasure_count=10):
        self.map_size = map_size
        self.treasure_count = treasure_count
        self.player_position = [0, 0]
        self.treasure_positions = []
        self.generate_map()

    def generate_map(self):
        self.player_position = [random.randint(0, self.map_size-1), random.randint(0, self.map_size-1)]
        self.treasure_positions = []
        while len(self.treasure_positions) < self.treasure_count:
            treasure_position = [random.randint(0, self.map_size-1), random.randint(0, self.map_size-1)]
            if treasure_position not in self.treasure_positions and treasure_position != self.player_position:
                self.treasure_positions.append(treasure_position)

    def move_player(self, direction):
        dx, dy = 0, 0
        if direction == "up" and self.player_position[1] > 0:
            dy = -1
        elif direction == "down" and self.player_position[1] < self.map_size - 1:
            dy = 1
        elif direction == "left" and self.player_position[0] > 0:
            dx = -1
        elif direction == "right" and self.player_position[0] < self.map_size - 1:
            dx = 1

        new_x = self.player_position[0] + dx
        new_y = self.player_position[1] + dy

        # Check if the new position is valid
        if 0 <= new_x < self.map_size and 0 <= new_y < self.map_size:
            self.player_position[0] = new_x
            self.player_position[1] = new_y

        self.check_collision()

    def check_collision(self):
        for treasure_position in self.treasure_positions:
            if treasure_position == self.player_position:
                self.treasure_positions.remove(treasure_position)
                if not self.treasure_positions:
                    messagebox.showinfo("Congratulations!", "You found all the treasures!")
                    self.generate_map()
                elif len(self.treasure_positions) % (self.treasure_count // 5) == 0:
                    messagebox.showinfo("Treasure Found!", f"{len(self.treasure_positions)} treasures left!")
                return  # Exit the method if a treasure is found
