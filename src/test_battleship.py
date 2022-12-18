# Battleship tests
from battleship import Game_map
from battleship import Player


# Test case: test_create_game_map() examines whether a game map has been built
# up or not.
# Expected behavior: If map was created, the length of 2D list should be
# bigger than 0 (not empty).
def test_create_game_map():
    test_map = Game_map()
    test_map.create_game_map()
    map = test_map.get_game_map()

    assert len(map) > 0


# Test case:test_game_map_row() examines the number of rows of the 2D list,
# which is the game map. This test checks the game map building as well.
# Expected behavior: 10 rows should be created, in case the map is successfully
# built up.
def test_game_map_row():
    test_map = Game_map()
    test_map.create_game_map()
    map = test_map.get_game_map()
    rows = 0
    for i in map:
        rows += 1
        print(rows)

    assert rows == 10


# Test case: test_carrier_placement() examines if the carrier ship is placed
# on the map. This test checks if the add_ships method works as intended.
# Expected behavior: 5 (map id for carrier) should be found in the game map
# list.
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
# Test case: examine ship length of the carrier. This test checks if the
# add_ships method works as intended.
# Expected behavior: 5 should appear 5 times in the list (game map)
def test_carrier_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(5) for row in map) == 5


# Test case: test_battleship_placement() examines if the battleship is placed
# on the map. This test checks if the add_ships method works as intended.
# Expected behavior: 4 (map id for battleship) should be found in the game map
# list.
def test_battleship_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(4 in sublist for sublist in map)  # the battleship
    # map_id is 4, so that is what I looked for


# Test case: examine ship length of the battleship. This test checks if the
# add_ships method works as intended.
# Expected behavior: 4 should appear 4 times in the list (game map)
def test_battleship_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(4) for row in map) == 4


# Test case: test_cruiser_placement() examines if the cruiser is placed
# on the map. This test checks if the add_ships method works as intended.
# Expected behavior: 3 (map id for cruiser) should be found in the game map
# list.
def test_cruiser_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(3 in sublist for sublist in map)  # The cruiser
    # ship map_id is 3, so that is what I looked for


# Test case: examine ship length of the cruiser. This test checks if the
# add_ships method works as intended.
# Expected behavior: 3 should appear 3 times in the list (game map)
def test_cruiser_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(3) for row in map) == 3


# Test case: test_destroyer_placement() examines if the destroyer is placed
# on the map. This test checks if the add_ships method works as intended.
# Expected behavior: 2 (map id for cruiser) should be found in the game map
# list.
def test_destroyer_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(2 in sublist for sublist in map)  # the destroyer
    # ship map_id is 2, so that is what I looked for in the map


# Test case: examine ship length of the destroyer. This test checks if the
# add_ships method works as intended.
# Expected behavior: 2 should appear 2 times in the list (game map)
def test_destroyer_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(2) for row in map) == 2


# Test case: test_submarine_placement() examines if the submarine is placed
# on the map. This test checks if the add_ships method works as intended.
# Expected behavior: 1 (map id for cruiser) should be found in the game map
# list.
def test_submarine_placement():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert any(1 in sublist for sublist in map)  # the submarine
    # map_id is 1, so that is what I looked for


# Test case: examine ship length of the submarine. This test checks if the
# add_ships method works as intended.
# Expected behavior: 1 should appear 3 times in the list (game map)
def test_submarine_length():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    map = test_map.get_game_map()
    assert sum(row.count(1) for row in map) == 3


# Test case: test_x_translator test x coordinate translator
# Expected behavior: based on the input first element (F), gives back the
# value pair that is assigned to the F key. In this case 5.
def test_x_translator():
    player = Player()
    test_coordinate = ['F', 4]
    x = player.x_coordinate_translator(test_coordinate)
    assert x == 5


# Test case: test_y_translator test y coordinate translator
# Expected behavior: based on the input second element (4), gives back a value
# that subtracted by 1. In this case it is 3.
def test_y_translator():
    player = Player()
    test_coordinate = ['F', 4]
    y = player.y_coordinate_translator(test_coordinate)
    assert y == 3


# Test case: test if map is updated after a missed shot, ships are not placed
# on the map, so we can be sure that it is a missed shot.
# This tests the shoot_and_feedback method
# Expected behavior, ~ will appear at the coordinates on the map.
def test_missed_shot():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.shoot_and_feedback(5, 4)
    map = test_map.get_game_map()
    assert map[4][5] == '~'


# Test case: test if map is updated after ships are placed and
# shoot_and_feedback method was called with coordinates.
# This tests the shoot_and_feedback method
# Expected behavior: The map has to be updated with a ~ or an X at the
# coordinates on the map.
def test_shot():
    test_map = Game_map()
    test_map.create_game_map()
    test_map.add_ships()
    test_map.shoot_and_feedback(5, 4)
    map = test_map.get_game_map()
    assert ((map[4][5] == '~') or (map[4][5] == 'X'))
