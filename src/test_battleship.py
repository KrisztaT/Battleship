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
