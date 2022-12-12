# Battleship tests
from battleship import Game_map


#  test_create_game_map() examines whether a game map has been built up
# or not. If it was, the length of list should be bigger than 0 (not empty).
def test_create_game_map():
    test_map = Game_map()
    test_map.create_game_map()
    map = test_map.get_game_map()

    assert len(map) > 0


# test_game_map_row() examines the number of rows of the 2D list, which is
# the game map. 10 rows should be created.
def test_game_map_row():
    test_map = Game_map()
    test_map.create_game_map()
    map = test_map.get_game_map()
    rows = 0
    for i in map:
        rows += 1
        print(rows)

    assert rows == 10


# test_carrier_placement() examines if the carrier ship is placed
# on the map
def test_carrier_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(5 in sublist for sublist in map)  # to check if an item is in
    # the 2D list, any is used, it returns True if item is found.
    # In this case the carrier ship map_id is 5, so that is what I looked for


# ships are placed in a continuos horizontal or vertical line, hence
# counting how many 5s (carrier ship id) can be seen in the map gives
# back the carrier's length (5)
def test_carrier_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(5) for row in map) == 5


# test_battleship_placement() examines if the battleship is placed on the map
def test_battleship_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(4 in sublist for sublist in map)  # the battleship
    # map_id is 4, so that is what I looked for


# Battleship length examination, ship length is 4.
def test_battleship_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(4) for row in map) == 4


# test_cruiser_placement() examines if the cruiser is placed on the map
def test_cruiser_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(3 in sublist for sublist in map)  # The cruiser
    # ship map_id is 3, so that is what I looked for


# Cruiser ship length examination, ship length is 3.
def test_cruiser_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(3) for row in map) == 3


# test_destroyer_placement() examines if the destroyer is placed on the map
def test_destroyer_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(2 in sublist for sublist in map)  # the destroyer
    # ship map_id is 2, so that is what I looked for in the map


# Destroyer ship length examination, ship length is 2.
def test_destroyer_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(2) for row in map) == 2
