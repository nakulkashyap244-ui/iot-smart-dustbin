from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

latest = {"fill": 0}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json() or {}
    latest["fill"] = data.get("fill", latest["fill"])
    return {"msg": "ok", "fill": latest["fill"]}

@app.route("/data")
def data():
    return jsonify({"fill": latest["fill"]})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
