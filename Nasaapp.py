from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route("/")
def mars_photos():
    r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key=DEMO_KEY')
    jsondata = json.loads(r.text)
    photos1 = jsondata['latest_photos']
    return render_template('index.html', photos = photos1)

app.run(debug=True)