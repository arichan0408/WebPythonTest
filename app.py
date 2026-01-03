from flask import Flask, request, render_template

app = Flask(__name__)

class Result:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b
        self.ave = self.sum / 2
         
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        result = Result(a, b)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
