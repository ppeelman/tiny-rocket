from db.config import db_session
from db.models.rocket import Rocket
import requests


def toRocket(rocket_data):
    return Rocket(name=rocket_data['name'],
                  description=rocket_data['description'],
                  success_rate_pct=rocket_data['success_rate_pct'])


class LoadRocketsFromApiUsecase:
    @staticmethod
    def execute():
        response = requests.get('https://api.spacexdata.com/v4/rockets')
        data = response.json()

        Rocket.query.delete()

        for rocket_data in data:
            db_session.add(toRocket(rocket_data))

        db_session.commit()
