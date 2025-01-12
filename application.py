from flask import Flask, render_template, redirect
from db.config import db_session
from db.models.rocket import Rocket
import requests

app = Flask(__name__)


@app.route("/")
def index():
    rockets = Rocket.query.all()
    return render_template('index.html', rockets=rockets)


@app.post("/load-rockets")
def load_rockets():
    response = requests.get('https://api.spacexdata.com/v4/rockets')
    data = response.json()

    Rocket.query.delete()

    for rocket_data in data:
        rocket_data = Rocket(name=rocket_data['name'],
                             description=rocket_data['description'],
                             success_rate_pct=rocket_data['success_rate_pct'])
        db_session.add(rocket_data)

    db_session.commit()

    return redirect("/", code=302)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
