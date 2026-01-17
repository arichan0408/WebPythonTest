from flask import Flask, request, render_template

from domain.models import Option, Player
from domain.calculator import MahjongCalculator

from viewmodels.yen_calculator import OptionView, PlayerView, ResultView

app = Flask(__name__)

rate_dict = {
    "1000点=10円": 10/1000,
    "1000点=20円": 20/1000,
    "1000点=50円": 50/1000,
    "1000点=100円": 100/1000
}

chip_rate_dict = {
    "1枚=100円": 100,
    "1枚=200円": 200,
    "1枚=500円": 500,
    "1枚=1000円": 1000,
}

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/yen_calculator", methods=["GET", "POST"])
def yen_calculator():
    result = None
    if request.method == "POST":
        # ===== フォーム -> domain =====
        option = Option(
            start_point=int(request.form["start_point"], 0),
            rate=rate_dict[request.form["rate"]],
            uma=request.form["uma"] == "1",
            oka=request.form["oka"] == "1",
            start_chip=int(request.form["start_chip"]),
            chip_rate=chip_rate_dict[request.form["chip_rate"]]
        )
        
        players = []
        for key in ["a", "b", "c", "d"]:
            players.append(
                Player(
                    name=request.form[f"{key}_name"],
                    point=int(request.form[f"{key}_point"]),
                    chip=int(request.form[f"{key}_chip"])
                )
            )

        # ===== domain 計算 =====
        mahjong_calculator = MahjongCalculator(option=option)
        players_results = [
            mahjong_calculator.calculate(player) for player in players
        ]

        # ===== domain -> viewmodel
        option_view = OptionView(
            start_point=option.start_point,
            rate=option.rate,
            uma=option.uma,
            oka=option.oka,
            start_chip=option.start_chip,
            chip_rate=option.chip_rate
        )

        players_view = [
            PlayerView(
                name=result.player.name,
                point=result.player.point,
                chip=result.player.chip,
                soten=result.soten,
                soten_yen=result.soten_yen,
                chip_yen=result.chip_yen,
                total_yen=result.total_yen
            )
            for result in players_results
        ]

        result = ResultView(option_view, players_view)

    return render_template("yen_calculator.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
