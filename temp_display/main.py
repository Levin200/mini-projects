import flask
from flask  import Flask, render_template, request
import weather

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/result.html", methods = ["POST"])
def result_page():
    place = request.form["place"]
    print(place)
    temp, feels_like = weather.weather(place)
    print(temp, feels_like)
    return render_template("result.html", temp = temp, feels_like = feels_like)


if __name__ == "__main__":
    app.run(debug=True)