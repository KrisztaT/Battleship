# BattleShip Lite
from tabulate import tabulate
from random import randint
from random import choice
from termcolor import cprint
from pyfiglet import figlet_format
import re
import os
import sys
import time


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

    # print the game map useful for visual test, it shows all the changes
    # different methods do on the map
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
        # comment screen clear out to test the app
        if (os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls||clear')
        print(tabulate(player_game_map, headers=headers, tablefmt='fancy_grid',
              showindex=range(1, self.rows + 1), stralign='center'))
        print(self.msg)

    # mainly for tdd purposes, gives back the game map
    def get_game_map(self):
        return self.game_map

    # add ships to the map
    def add_ships(self):
        self.ships = [Carrier(), Battleship(), Cruiser(),
                      Submarine(), Destroyer()]

        # random orientation and coordinate generation
        def generate_random_location(self):
            self.orientation = choice(['H', 'V'])
            self.rnd_x = randint(0, 9)
            self.rnd_y = randint(0, 9)

        # add ships to the map based on id, it examines overlay and hang off
        for ship in self.ships:
            len = ship.get_length()
            is_grid_free = False
            while not is_grid_free:
                is_grid_free = True
                generate_random_location(self)
                if self.orientation == 'H':
                    for j in range(len):
                        # try-except block is used, because random generation
                        # might result in a coordinate that leads to the ship
                        # hang off the map. So in that case an IndexError is
                        # thrown, the except block handle that with giving the
                        # is_grid_free variable a False value, so a new
                        # location generation is triggered within the while
                        # loop
                        try:
                            if self.game_map[self.rnd_y][self.rnd_x + j] != 0:
                                is_grid_free = False
                        except IndexError:
                            is_grid_free = False
                else:
                    for j in range(len):
                        try:
                            if self.game_map[self.rnd_y + j][self.rnd_x] != 0:
                                is_grid_free = False
                        except IndexError:
                            is_grid_free = False

            if self.orientation == 'H':
                for j in range(len):
                    id = ship.get_map_id()
                    self.game_map[self.rnd_y][self.rnd_x + j] = id
            else:
                for j in range(len):
                    id = ship.get_map_id()
                    self.game_map[self.rnd_y + j][self.rnd_x] = id

    # shoot and feedback method examine the coordinate coming from the
    # handle_shot_coordinates method in the Player class
    # if there is a ~ or X it means there was a shot there before, so the app
    # gives back the message Already shot there!
    # if there was no ship on the map (0) at the shot coordinate before
    # then puts a ~ in the map to that coordinate and gives the message Missed
    # if there is a ship on the map (1,2,3,4,5) at the shot coordinate
    # then puts an X in the map to that coordinate and gives the message
    # which ship was hit and how much life it has, or if a ship were sunk,
    # it is also printed
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
                self.msg = 'Hit a ' + ship_name + ' that has ' \
                            + str(ship_life) + ' life left.'
            else:
                self.msg = 'Good Job! You have sunk a ' + ship_name + "."
        self.print_user_game_map()

    # check if any ship is still alive
    def check_any_ship_alive(self):
        for ship in self.ships:
            if ship.get_alive():
                return True
        return False


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
    # examining if the ship life is 0, in that case the ship
    # is_alive variable gets the False value
    def decrease_life(self):
        self.life -= 1
        if self.life == 0:
            self.is_alive = False

    def get_map_id(self):
        return self.map_id

    def get_alive(self):
        return self.is_alive


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
        self.shot_count = 0

    # greet player method asks for the player's name first, check it against
    # the regex pattern: name can contain upper and lower cases, space,
    # underscore, and hyphen and it has to be between 2 and 25 characters long.
    # In case the name is invalid a ValueError is raised and a new
    # name needs to be typed in. After a valid name is given, a greeting, that
    # includes the user name, is printed. To test error handling provide name
    # such as *Name , This will be a very long user name for test etc.
    def greet_player(self):
        cprint(figlet_format('Battleship Lite'), 'blue', attrs=['bold'])
        while True:
            try:
                self.name = input("Please enter your name: ")
                if (bool(re.fullmatch('^[a-zA-Z0-9 _-]{2,25}+$', self.name))):
                    break
                else:
                    raise ValueError
            except ValueError:
                cprint('The name is not valid!', 'red')
                continue
        cprint(f'Hello {self.name}, let\'s start the game!', 'green')
        time.sleep(3)

    # handle shot coordinates ask for user input about the coordinates
    # translate given coordinates to 2D list indexes
    # runs until ships are alive
    # to test the error handling try to use coordinates such as (a,a , a,12,
    # 1,2, dhjsgfas etc. )
    def handle_shot_coordinates(self, map):
        while map.check_any_ship_alive():
            try:
                coordinates = input('Please enter a coordinate (i.e.: A,5) or '
                                    + 'x to exit: ')
                if coordinates == 'x' or coordinates == 'X':
                    sys.exit('You chose to exit the game. Bye!')
                else:
                    coordinates_list = coordinates.split(',')
                    x = self.x_coordinate_translator(coordinates_list)
                    y = self.y_coordinate_translator(coordinates_list)
                    if y < 0:
                        raise IndexError
                    self.shot_count += 1
                    # uncomment print if you want to see the coordinates
                    # print(x, y, self.shot_count)
                    map.shoot_and_feedback(x, y)
            except (UnboundLocalError, IndexError, ValueError):
                cprint('Please enter a valid coordinate.', 'red')
                continue

        print(f'{self.name}, you used {self.shot_count} shots to sunk all'
              + ' the ships!')
        cprint(figlet_format('Congratulations!'), 'green', attrs=['bold'])

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

    # to visually test if the ships were placed, run the commented code below
    # game_map.print_game_map()

    game_map.print_user_game_map()
    player.handle_shot_coordinates(game_map)


# Allow file execution when it is not an imported module.
if __name__ == "__main__":
    main()
