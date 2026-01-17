from domain.models import Option, Player, MahjongCalculatorResult

class MahjongCalculator:
    def __init__(self, option: Option):
        self.option = option
    
    def calculate(self, player: Player) -> MahjongCalculatorResult:
        soten = player.point - self.option.start_point
        soten_yen = soten * self.option.rate
        chip = player.chip - self.option.start_chip
        chip_yen = chip * self.option.chip_rate
        total_yen = soten_yen + chip_yen

        return MahjongCalculatorResult(player, soten, soten_yen, chip_yen, total_yen)