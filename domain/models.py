from dataclasses import dataclass

@dataclass
class Player:
    name: str
    point: int
    chip: int

@dataclass
class Option:
    start_point: int
    rate: float
    uma: bool
    oka: bool
    start_chip: int
    chip_rate: float

@dataclass
class MahjongCalculatorResult:
    player: Player
    soten: int
    soten_yen: int
    chip_yen: int
    total_yen: int