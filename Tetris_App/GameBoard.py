from typing import List
from Tetris_App.Tile import Tile, Coordinates, TileColor

class GameBoard():
    def __init(self, width: int, height: int):
        self._width: int = width
        self._height: int = height
        self._tiles: List[List[Tile]] = self._create_tiles()
        self._board_changed = True

    @property
    def Tiles(self):
        return self._tiles
    
    @property
    def BoardChanged(self):
        return self._board_changed
        
    def is_position_occupied(self, tile: Tile) -> bool:
        if (tile.Position.X < 0 or tile.Position.X >= self._width or tile.Position.Y < 0 or tile.Position.Y >= self._height):
            return True
        
        return self._tiles[tile.Position.X][tile.Position.Y].Color is not TileColor.Transparent
    
    def set_tiles(self, tiles List[Tile]) -> None:
        for tile in tiles:
            self._tiles[tile.Position.X][tile.Position.Y] = tile

        self._board_changed = True

    def _create_tiles(self) -> List[List[Tile]]:
        return [[Tile(Coordinates(x,y), TileColor.Transparent) for y in range(self._width)] for x in range(self._height)]
