import gameoflife


def test_gmeoflfe_display_dead():
    assert gameoflife.display_grid([[1,1,1],[1,1,1],[1,1,1,]]) == '111\n111\n111'

def test_gmeoflfe_display_dead_live():
    assert gameoflife.display_grid([[1,1,1],[1,1,0],[1,1,0]]) == '111\n110\n110'



# def test_gmeoflfe_play():
#       assert gameoflife.ply_game([[1,1,1,1,1],[1,1,1,0,1],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1]]) == '#####\n#####\n#####\n#####\n#####\n'

def sample_board():
    return [[0,1,0],[0,0,1],[1,1,1]]

def test_next_live_or_dead():
    expected_board = [[0,0,0],[1,0,1],[0,1,1]]
    assert gameoflife.next_generation(sample_board) == expected_board