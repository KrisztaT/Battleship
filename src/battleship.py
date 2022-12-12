# BattleShip Lite
from tabulate import tabulate
from random import randint
from random import choice
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

    def print_user_game_map(self):
        headers = 'ABCDEFGHIJ'
        player_game_map = [['']*self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                match (self.game_map[i][j]):
                    case 0 | 1 | 2 | 3 | 4 | 5: player_game_map[i][j] = ''
                    case 'X': player_game_map[i][j] = 'X'
                    case '~': player_game_map[i][j] = '~'
        print(tabulate(player_game_map, headers=headers, tablefmt='fancy_grid',
              showindex=range(1, self.rows + 1), stralign='center'))

    # mainly for test purposes, gives back the game map
    def get_game_map(self):
        return self.game_map

    # add ships to the map
    def add_ships(self):
        self.ships = [Carrier(), Battleship(), Cruiser(),
                      Submarine(), Destroyer()]

        # random orientation and coordinate generation
        def generate_random_location(self):
            self.orientation = choice(['H', 'V'])
            self.rand_x = randint(0, 9 - len)
            self.rand_y = randint(0, 9 - len)

        # add ships to the map based on id, no overlap examination yet
        for ship in self.ships:
            len = ship.get_length()
            is_grid_free = False
            while not is_grid_free:
                is_grid_free = True
                generate_random_location(self)
                if self.orientation == 'H':
                    for j in range(len):
                        if self.game_map[self.rand_y][self.rand_x + j] != 0:
                            is_grid_free = False
                else:
                    for j in range(len):
                        if self.game_map[self.rand_y + j][self.rand_x] != 0:
                            is_grid_free = False

            if self.orientation == 'H':
                for j in range(len):
                    id = ship.get_map_id()
                    self.game_map[self.rand_y][self.rand_x + j] = id
            else:
                for j in range(len):
                    id = ship.get_map_id()
                    self.game_map[self.rand_y + j][self.rand_x] = id


# parent Ships class is defined with properties that all ships have common
# also getters for the properties were added for use of other methods
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

    # decrease_life method is for decrease ship life once it was hit.
    def decrease_life(self):
        self.life -= 1

    def get_map_id(self):
        return self.map_id


# Each different ships has its own class with individual property values
# and all inherits property and methods from Ships
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
                self.name = input("Please enter your name: ")
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
    game_map = Game_map()
    game_map.create_game_map()
    game_map.add_ships()
    game_map.print_game_map()
    game_map.print_user_game_map()


# Allow file execution when it is not an imported module.
if __name__ == "__main__":
    main()
