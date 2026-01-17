from dataclasses import dataclass

@dataclass
class OptionView:
    start_point: int
    rate: float
    uma: bool
    oka: bool
    start_chip: int
    chip_rate: float

@dataclass
class PlayerView:
    name: str
    point: int
    chip: int
    soten: int
    soten_yen: int
    chip_yen: int
    total_yen: int

@dataclass
class ResultView:
    option: OptionView
    players: list[PlayerView]

