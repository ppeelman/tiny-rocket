from flask import Flask, render_template, jsonify, request

from db.config import db_session
from usecase.fetch_all_launches import FetchAllLaunchesUsecase
from usecase.load_rockets_from_api import LoadRocketsFromApiUsecase
from usecase.get_all_rockets import GetAllRocketsUsecase

app = Flask(__name__)


@app.route("/")
def index():
    page = request.args.get('page')

    launches = FetchAllLaunchesUsecase.execute(page)

    context = {
        'launches': launches["docs"],
        'next_page': launches["nextPage"],
        'previous_page': launches["prevPage"]
    }
    return render_template('index.html', **context)


@app.route("/rockets")
def rockets_view():
    rockets = GetAllRocketsUsecase.execute()
    return render_template('rockets.html', rockets=rockets)


# =======================================================
# API endpoints
# =======================================================

@app.get("/api/launches")
def get_all_launches():
    page = request.args.get('page')
    launches = FetchAllLaunchesUsecase.execute(page)
    return jsonify(launches)


@app.get("/api/rockets")
def get_all_rockets():
    rockets = GetAllRocketsUsecase.execute()
    rockets_presented = [rocket.toPresented() for rocket in rockets]
    return jsonify(rockets_presented)


@app.post("/api/load-rockets")
def load_rockets():
    LoadRocketsFromApiUsecase.execute()
    return "Rockets successfully loaded into database!"


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
