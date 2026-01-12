from flask import Flask, request, render_template

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

class Option:
    def __init__(self, start_point=25000, rate=rate_dict["1000点=10円"], uma=True, oka=True, start_chip=0, chip_rate=chip_rate_dict["1枚=100円"]):
        self.start_point = start_point
        self.rate = rate
        self.uma = uma
        self.oka = oka
        self.start_chip = start_chip
        self.chip_rate = chip_rate

class Player:
    def __init__(self, option, name, value, chip):
        self.name = name
        self.value = value
        self.soten = self.value - option.start_point
        self.soten2en = self.soten * option.rate
        self.chip = chip - option.start_chip
        self.chip2en = self.chip * option.chip_rate

        self.sum = self.soten2en + self.chip2en

class Result:
    def __init__(self, option, a, b, c, d):
        self.option = option
        self.a = a
        self.b = b
        self.c = c
        self.d = d
         
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        option = Option(
            int(request.form["start_point"]),
            rate_dict[str(request.form["rate"])],
            bool(request.form["uma"]),
            bool(request.form["oka"]),
            int(request.form["start_chip"]),
            chip_rate_dict[str(request.form["chip_rate"])]
            )
        a = Player(option, str(request.form["a_name"]), int(request.form["a_value"]), int(request.form["a_chip"]) )
        b = Player(option, str(request.form["b_name"]), int(request.form["b_value"]), int(request.form["b_chip"]) )
        c = Player(option, str(request.form["c_name"]), int(request.form["c_value"]), int(request.form["c_chip"]) )
        d = Player(option, str(request.form["d_name"]), int(request.form["d_value"]), int(request.form["d_chip"]) )
        result = Result(option, a, b, c, d)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
