from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# global besked
current_message = ""

@app.route("/")
def index():
    return render_template("index.html", message=current_message)

@app.route("/set_message", methods=["POST"])
def set_message():
    global current_message
    data = request.get_json()
    current_message = data.get("message", "")
    return jsonify(success=True, message=current_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
