from lib import blocks

def test_the_creation_of_a_grid():
    # A grid holds the colors of the squares

    # We need a map to return that color, which is just blue for now, but it does use a function to return it just in case we want to randomize the colors, which we do in reality
    color_map = {'blue': lambda: (1, 128, 1)}

    assert(len(blocks.create_grid(3, 3, color_map)) == 3)

