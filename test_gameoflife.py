import gameoflife

def test_gmeoflfe_display_dead():
    assert gameoflife.display_grid([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == '#####\n#####\n#####\n#####\n#####'

def test_gmeoflfe_display_dead_live():
    assert gameoflife.display_grid([[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,0,1]]) == '#####\n##.##\n##.##\n#####\n###.#'



# def test_gmeoflfe_play():
#       assert gameoflife.ply_game([[1,1,1,1,1],[1,1,1,0,1],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1]]) == '#####\n#####\n#####\n#####\n#####\n'
