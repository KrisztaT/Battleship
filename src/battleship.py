# BattleShip Lite
from tabulate import tabulate
import re


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


class Ships:
    def __init__(self, ship_type, length, map_id) -> None:
        self.ship_type = ship_type
        self.length = length
        self.life = length
        self.map_id = map_id
        self.is_alive = True

    def get_ship_type(self):
        return self.ship_type

    def get_length(self):
        return self.length

    def get_life(self):
        return self.life

    def decrease_life(self):
        self.life -= 1

    def get_map_id(self):
        return self.map_id


class Carrier(Ships):
    def __init__(self, map_id=5) -> None:
        super().__init__('carrier', 5, map_id)


class Battleship(Ships):
    def __init__(self, map_id=4) -> None:
        super().__init__('battleship', 4, map_id)


class Cruiser(Ships):
    def __init__(self, map_id=3) -> None:
        super().__init__('cruiser', 3, map_id)


class Submarine(Ships):
    def __init__(self, map_id=1) -> None:
        super().__init__('submarine', 3, map_id)


class Destroyer(Ships):
    def __init__(self, map_id=2) -> None:
        super().__init__('destroyer', 2, map_id)


# Player class is created with the Player's name as a property.
class Player:
    def __init__(self) -> None:
        self.name = ""

    # Greet player method asks for the player's name first, check it against
    # the regex pattern: name can contain upper and lower cases, space,
    # underscore, and hyphen and it has to be between 2 and 25 characters long.
    # In case the name is invalid a ValueError is raised and a new
    # name needs to be typed in. After a valid name is given, a greeting, that
    # includes the user name, is printed.
    def greet_player(self):
        while True:
            try:
                self.name = input("Please enter your name :")
                if (bool(re.fullmatch('^[a-zA-Z0-9 _-]{2,25}+$', self.name))):
                    break
                else:
                    raise ValueError
            except ValueError:
                print('The name is not valid!')
                continue
        print(f'Hello {self.name}, let\'s start the game!')


# Game control
def main():
    # Create player object and call its methods to greet the player
    player = Player()
    player.greet_player()
    # Create game map object and call its methods to create and print game map
    """ game_map = Game_map()
    game_map.create_game_map()
    game_map.print_game_map() """


# Allow file execution when it is not an imported module.
if __name__ == "__main__":
    main()
