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
    temp, feels_like,description, icon = weather.weather(place)
    icon_url =  "https://openweathermap.org/img/wn/" + icon + "@2x.png"
    print(icon, icon_url)
    return render_template("result.html", temp = temp, feels_like = feels_like, place = place, icon = icon_url, description= description.capitalize())


if __name__ == "__main__":
    app.run(debug=True)