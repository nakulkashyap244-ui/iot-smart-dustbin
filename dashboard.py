from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Dustbin Dashboard</title>
    <style>
        body {
            font-family: Arial;
            background: #f3f3f3;
            padding: 20px;
        }
        .box {
            background: white;
            padding: 20px;
            width: 300px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <h2>Smart Dustbin Dashboard</h2>
    <div class="box">
        <p>Status: Working</p>
        <p>Fill Level: 40%</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True, port=5001)