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
        self.ships = []
        self.msg = ''

    # create game map, filled with zeros
    def create_game_map(self):
        self.game_map = [[0]*self.cols for _ in range(self.rows)]

    # print the game map useful for visual test
    def print_game_map(self):
        headers = 'ABCDEFGHIJ'
        print(tabulate(self.game_map, headers=headers, tablefmt='fancy_grid',
              showindex=range(1, self.rows + 1)))

    # print game map for user it hides the ships, in case of miss ~
    # will be put in the map, in case of hit X.
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
        print(self.msg)

    # mainly for test purposes, gives back the game map
    def get_game_map(self):
        return self.game_map

    # add ships to the map
    def add_ships(self):
        self.ships = [Carrier(), Battleship(), Cruiser(),
                      Submarine(), Destroyer()]

        # random orientation and coordinate generation
        # it does not allow the generation of out of range coordinates
        def generate_random_location(self):
            self.orientation = choice(['H', 'V'])
            self.rand_x = randint(0, 9 - len)
            self.rand_y = randint(0, 9 - len)

        # add ships to the map based on id, it examines overlay
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

    # shoot and feedback method examine the coordinate coming from the
    # handle_shot_coordinates method in the Player class
    # if there is a ~ or X it means there was a shot there before, so the app
    # gives back the message Already shot there!
    # if there was no ship on the map (0) at the shot coordinate before
    # then puts a ~ in the map to that coordinate and gives the message Missed
    # if there is a ship on the map (1,2,3,4,5) at the shot coordinate
    # then puts an X in the map to that coordinate and gives the message Hit
    def shoot_and_feedback(self, x, y):
        if (self.game_map[y][x] == '~' or self.game_map[y][x] == 'X'):
            self.msg = 'Already shot there!'
        elif (int(self.game_map[y][x]) == 0):
            self.game_map[y][x] = '~'
            self.msg = 'Missed'
        elif (int(self.game_map[y][x]) > 0):
            for ship in self.ships:
                if (ship.get_map_id() == self.game_map[y][x]):
                    ship_name = ship.get_ship_type()
                    ship.decrease_life()
                    ship_life = ship.get_life()
            self.game_map[y][x] = 'X'
            if (ship_life > 0):
                self.msg = 'Hit a ' + ship_name + ' that has ' + str(ship_life) + ' life left.'
            else:
                self.msg = 'Good Job! You sunk a ' + ship_name + "."
        self.print_user_game_map()


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

    # handle shot coordinates ask for user input about the coordinates
    # translate given coordinates to 2D list indexes
    def handle_shot_coordinates(self, map):
        # until the appropriate loop condition can not be added, for test
        # it is defined like this
        i = 0
        while (i < 5):
            try:
                coordinates = input('Enter the coordinates (i.e.: A,5): ')
                coordinates_list = coordinates.split(',')
                x = self.x_coordinate_translator(coordinates_list)
                y = self.y_coordinate_translator(coordinates_list)
                if y < 0:
                    raise IndexError
                map.shoot_and_feedback(x, y)
                i += 1
            except (UnboundLocalError, IndexError, ValueError):
                print('Please enter valid coordinates (i.e.: A,5).')
                continue

    # translate the the first element of coordinate_ list
    # i.e.: B to list index which is 1 in case of B.
    def x_coordinate_translator(self, coordinate_list):
        x_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                  "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

        if coordinate_list[0].upper() in x_dict.keys():
            x = x_dict[coordinate_list[0].upper()]
        return x

    # translate the second element of the coordinate_ list
    # i.e.: 3, as list index starts from 0 it is 2.
    def y_coordinate_translator(self, coordinate_list):
        y = int(coordinate_list[1]) - 1
        return y


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
    player.handle_shot_coordinates(game_map)


# Allow file execution when it is not an imported module.
if __name__ == "__main__":
    main()
