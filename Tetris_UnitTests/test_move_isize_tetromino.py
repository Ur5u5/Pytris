from dataclasses import asdict
from pyparsing import Any
import pytest
from typing import List

from Tetris_App.ISizeRotationStates import ISizeRotationState0Degree
from Tetris_App.Tetromino import Tetromino
from Tetris_App.TetrominoMover import GameBoard, TetrominoMover
from Tetris_App.Tile import Tile, Coordinates, TileColor

@pytest.fixture
def test_setup():
    class MoverTestsSetup():
        _width: int = 10
        _height: int = 20

        def __init__(self):
            pass

        def create_tetromino_mover(self) -> TetrominoMover:
            return TetrominoMover(GameBoard(self._width, self._height))
        
        def create_tetromino_at(self, offset: Coordinates) -> Tetromino:
            result: Tetromino = Tetromino(ISizeRotationState0Degree())
            result.Tiles = [
                Tile(Coordinates(offset.X, offset.Y), TileColor.Lightblue),
                Tile(Coordinates(offset.X + 1, offset.Y), TileColor.Lightblue),
                Tile(Coordinates(offset.X + 2, offset.Y), TileColor.Lightblue),
                Tile(Coordinates(offset.X + 3, offset.Y), TileColor.Lightblue)
            ]
            return result
        
        def create_game_board_bottom_occupied(self) -> GameBoard:
            occupiedTiles: List[Tile] = [Tile(Coordinates(x,self._width-1), TileColor.Red) for x in range(self._width)]
            result: GameBoard = GameBoard(self._width, self._height)
            result.set_tiles(occupiedTiles)
            return result
            
    return MoverTestsSetup()

@pytest.fixture
def mover(test_setup):
    return test_setup.create_tetromino_mover()

def are_values_equal(list1: List[Any], list2: List[Any]) -> bool:
    return [asdict(x) for x in list1] == [asdict(x) for x in list2]

@pytest.mark.parametrize(
        "offset, expected_tiles",
        [
            (
                Coordinates(5, 0),
                [
                    Tile(Coordinates(6, 0), TileColor.Lightblue),
                    Tile(Coordinates(7, 0), TileColor.Lightblue),
                    Tile(Coordinates(8, 0), TileColor.Lightblue),
                    Tile(Coordinates(9, 0), TileColor.Lightblue)]
            ),
            (
                Coordinates(6, 0),
                [
                    Tile(Coordinates(6, 0), TileColor.Lightblue),
                    Tile(Coordinates(7, 0), TileColor.Lightblue),
                    Tile(Coordinates(8, 0), TileColor.Lightblue),
                    Tile(Coordinates(9, 0), TileColor.Lightblue)]
            )
        ],
        ids=["Right_Inside_Boundary", "Right_Outside_Boundary"]
)
def test_move_right_boundary_check(test_setup, mover, offset, expected_tiles):
    tetromino: Tetromino = test_setup.create_tetromino_at(offset)

    mover.move_right(tetromino)

    assert are_values_equal(tetromino.Tiles, expected_tiles)

@pytest.mark.parametrize(
        "offset, expected_tiles",
        [
            (
                Coordinates(1, 0),
                [
                    Tile(Coordinates(0, 0), TileColor.Lightblue),
                    Tile(Coordinates(1, 0), TileColor.Lightblue),
                    Tile(Coordinates(2, 0), TileColor.Lightblue),
                    Tile(Coordinates(3, 0), TileColor.Lightblue)]
            ),
            (
                Coordinates(0, 0),
                [
                    Tile(Coordinates(0, 0), TileColor.Lightblue),
                    Tile(Coordinates(1, 0), TileColor.Lightblue),
                    Tile(Coordinates(2, 0), TileColor.Lightblue),
                    Tile(Coordinates(3, 0), TileColor.Lightblue)]
            )
        ],
        ids=["Left_Inside_Boundary", "Left_Outside_Boundary"]
)
def test_move_left_boundary_check(test_setup, mover, offset, expected_tiles):
    tetromino: Tetromino = test_setup.create_tetromino_at(offset)

    mover.move_left(tetromino)

    assert are_values_equal(tetromino.Tiles, expected_tiles)

def test_moveDown_noCollision_newPosition(test_setup, mover):
    tetromino: Tetromino = test_setup.create_tetromino_at(Coordinates(0, 17))
    expected_tiles: List[Tile] =  [
                    Tile(Coordinates(0, 18), TileColor.Lightblue),
                    Tile(Coordinates(1, 18), TileColor.Lightblue),
                    Tile(Coordinates(2, 18), TileColor.Lightblue),
                    Tile(Coordinates(3, 18), TileColor.Lightblue)]

    mover.move_down(tetromino)

    assert are_values_equal(tetromino.Tiles, expected_tiles)
    assert all(mover._gameBoard.Tiles[tile.Position.X][tile.Position.Y].Color is TileColor.Transparent for tile in tetromino.Tiles)

def test_moveDown_SetTetromino_AfterCollisionWithOccupiedTile(test_setup):
    gameBoard: GameBoard = test_setup.create_game_board_bottom_occupied()
    gameBoard.BoardChanged = False
    mover = TetrominoMover(gameBoard)
    tetromino = test_setup.create_tetromino_at(Coordinates(0, 19))

    mover.move_down(tetromino)

    for tile in tetromino.Tiles:
        assert asdict(tile) == asdict(gameBoard.Tiles[tile.Position.X][tile.Position.Y])
    
    assert gameBoard.BoardChanged is True