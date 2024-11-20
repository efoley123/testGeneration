import pytest
from unittest.mock import patch
from tictactoegame import TicTacToe
#from calc import main

@pytest.fixture
def tic_tac_toe_game():
    return TicTacToe()

def test_initialization():
    game = TicTacToe()
    assert game.board_size == 3
    assert game.board == [' ' for _ in range(9)]
    assert game.current_winner is None
    assert game.move_history == []
    assert game.scores == {'X': 0, 'O': 0, 'Draws': 0}
    assert game.current_player == 'X'

def test_validate_move_valid(tic_tac_toe_game):
    valid, message = tic_tac_toe_game.validate_move(0)
    assert valid is True
    assert message == "Valid move"

def test_validate_move_invalid_out_of_bounds(tic_tac_toe_game):
    valid, message = tic_tac_toe_game.validate_move(-1)
    assert valid is False
    assert message == "Move must be between 0 and 8"

def test_validate_move_invalid_occupied_square(tic_tac_toe_game):
    tic_tac_toe_game.board[0] = 'X'
    valid, message = tic_tac_toe_game.validate_move(0)
    assert valid is False
    assert message == "Square already occupied"

def test_make_move_success(tic_tac_toe_game):
    success, message = tic_tac_toe_game.make_move(0)
    assert success is True
    assert tic_tac_toe_game.board[0] == 'X'
    assert message == "Move successful"

def test_make_move_fail(tic_tac_toe_game):
    tic_tac_toe_game.board[0] = 'X'
    success, message = tic_tac_toe_game.make_move(0)
    assert success is False
    assert message == "Square already occupied"

def test_undo_move_success(tic_tac_toe_game):
    tic_tac_toe_game.make_move(0)
    success, message = tic_tac_toe_game.undo_move()
    assert success is True
    assert message == "Last move undone."
    assert tic_tac_toe_game.board[0] == ' '

def test_undo_move_fail_no_moves(tic_tac_toe_game):
    success, message = tic_tac_toe_game.undo_move()
    assert success is False
    assert message == "No moves to undo."

def test_check_winner_no_winner(tic_tac_toe_game):
    tic_tac_toe_game.make_move(0)  # X move
    tic_tac_toe_game.make_move(1)  # O move
    assert tic_tac_toe_game.check_winner(1) is False

def test_check_winner_with_winner(tic_tac_toe_game):
    for i in range(3):
        tic_tac_toe_game.make_move(i)  # X move
    assert tic_tac_toe_game.check_winner(2) is True

def test_available_moves_initial(tic_tac_toe_game):
    assert tic_tac_toe_game.available_moves() == list(range(9))

def test_available_moves_after_move(tic_tac_toe_game):
    tic_tac_toe_game.make_move(0)
    assert 0 not in tic_tac_toe_game.available_moves()

def test_is_board_full_false_initially(tic_tac_toe_game):
    assert tic_tac_toe_game.is_board_full() is False

def test_is_board_full_true_after_filling(tic_tac_toe_game):
    for i in range(9):
        tic_tac_toe_game.make_move(i)
    assert tic_tac_toe_game.is_board_full() is True

@pytest.mark.parametrize("input,expected", [
    (-1, False),
    (9, False),
    (4, True),
])
def test_validate_move_edge_cases(tic_tac_toe_game, input, expected):
    valid, _ = tic_tac_toe_game.validate_move(input)
    assert valid is expected

@patch('builtins.print')
def test_reset_game(mock_print, tic_tac_toe_game):
    tic_tac_toe_game.reset_game()
    assert tic_tac_toe_game.board == [' ' for _ in range(9)]
    assert tic_tac_toe_game.current_winner is None
    assert mock_print.called

@patch('random.choice')
def test_suggest_move(mock_choice, tic_tac_toe_game):
    mock_choice.return_value = 0
    assert tic_tac_toe_game.suggest_move() == 0

@patch('json.dump')
@patch('builtins.open', new_callable=pytest.mock_open)
def test_save_game(mock_open, mock_json_dump, tic_tac_toe_game):
    tic_tac_toe_game.save_game()
    mock_open.assert_called_with("tictactoe_save.json", "w")
    mock_json_dump.assert_called()

@patch('builtins.print')
@patch('json.load')
@patch('builtins.open', new_callable=pytest.mock_open, read_data='{"board": "         ", "scores": {"X": 0, "O": 0, "Draws": 0}, "current_player": "X", "move_history": []}')
def test_load_game(mock_open, mock_json_load, mock_print, tic_tac_toe_game):
    mock_json_load.return_value = {
        "board": [' ' for _ in range(9)],
        "scores": {'X': 0, 'O': 0, 'Draws': 0},
        "current_player": 'X',
        "move_history": []
    }
    tic_tac_toe_game.load_game()
    mock_open.assert_called_with("tictactoe_save.json", "r")
    assert mock_print.called