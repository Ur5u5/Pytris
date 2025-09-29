from typing import List
from Tetris_App.GameBoard import GameBoard
from Tetris_App.Tetromino import Tetromino
from Tetris_App.Tile import Coordinates, Tile


class TetrominoMover():
    _gameBoard: GameBoard

    def __init__(self, gameBoard: GameBoard) -> None:
        self._gameBoard = gameBoard

    def move_right(self, tetromino: Tetromino) -> None:
        next_position: List[Tile] = [
            Tile(Coordinates(tile.Position.X + 1, tile.Position.Y), tile.Color)
            for tile in tetromino.Tiles
        ]

        if (self._can_move(next_position)):
            tetromino.Tiles = next_position

    def move_left(self, tetromino: Tetromino) -> None:
        next_position: List[Tile] = [
            Tile(Coordinates(tile.Position.X - 1, tile.Position.Y), tile.Color)
            for tile in tetromino.Tiles 
        ]

        if (self._can_move(next_position)):
            tetromino.Tiles = next_position

    def move_down(self, tetromino: Tetromino) -> None:
        next_position: List[Tile] = [
        Tile(Coordinates(tile.Position.X, tile.Position.Y + 1), tile.Color)
        for tile in tetromino.Tiles 
    ]

        if (self._can_move(next_position)):
            tetromino.Tiles = next_position

        else:
            self._gameBoard.set_tiles(tetromino.Tiles)


    def fall_down(self, tetromino: Tetromino) -> None:
        while (not self._gameBoard.BoardChanged):
            self.move_down(tetromino)

    def rotate_right(self, tetromino: Tetromino) -> None:
        nextPosition: List[Tile] = tetromino.get_next_tile_positions()

        if (self._can_move(nextPosition)):
            tetromino.Tiles = nextPosition
            tetromino.rotate_right()

    def rotate_left(self, tetromino: Tetromino) -> None:
        nextPosition: List[Tile] = tetromino.get_previous_tile_positions()

        if (self._can_move(nextPosition)):
            tetromino.Tiles = nextPosition
            tetromino.rotate_left

    def _can_move(self, nextPosition: List[Tile]):
        return not any(self._gameBoard.is_position_occupied(tile) for tile in nextPosition)