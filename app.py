from flask import Flask, render_template, jsonify
from system_monitor import get_system_info

app = Flask(__name__)

@app.route("/")
def home():
    data = get_system_info()
    return render_template("index.html", data=data)
@app.route("/api/system")
def api_system():
    return jsonify(get_system_info())
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=False)