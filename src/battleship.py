# BattleShip Lite
from tabulate import tabulate


# First, a Game map class is created, properties rows, cols also a game_map
# list is initialised. The map will be a state map it is filled with zeros
# as a start, zero means no ship, no shot, no hit.
class Game_map:
    def __init__(self, rows=10, cols=10) -> None:
        self.rows = rows
        self.cols = cols
        self.game_map = []

    # create game map, filled with zeros
    def create_game_map(self):
        self.game_map = [[0]*self.cols for _ in range(self.rows)]

    # print the game map
    def print_game_map(self):
        headers = 'ABCDEFGHIJ'
        print(tabulate(self.game_map, headers=headers, tablefmt='fancy_grid',
              showindex=range(1, self.rows + 1)))

    # mainly for test purposes, gives back the game map
    def get_game_map(self):
        return self.game_map


# game control
def main():
    # create game map object and call its methods to create and print game map
    game_map = Game_map()
    game_map.create_game_map()
    game_map.print_game_map()


# Allow file execution when it is not an imported module.
if __name__ == "__main__":
    main()
