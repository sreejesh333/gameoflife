import gameoflife

def test_gmeoflfe_display():
    assert gameoflife.display_grid([[1,1,1,0,1],[1,1,1,0,1],[1,1,1,0,1],[1,1,1,0,1],[1,1,1,0,1]]) == '###.#\n###.#\n###.#\n###.#\n###.#\n'