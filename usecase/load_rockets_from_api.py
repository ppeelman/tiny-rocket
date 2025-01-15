from db.config import db_session
from db.models.rocket import Rocket
import requests


def toRocket(rocket_data):
    return Rocket(name=rocket_data['name'],
                  description=rocket_data['description'],
                  success_rate_pct=rocket_data['success_rate_pct'])


class LoadRocketsFromApiUsecase:
    API_URL = "https://api.spacexdata.com/v4/rockets"

    @staticmethod
    def execute():
        try:
            response = requests.get(LoadRocketsFromApiUsecase.API_URL)
            response.raise_for_status()
            data = response.json()

            Rocket.query.delete()

            for rocket_data in data:
                db_session.add(toRocket(rocket_data))

            db_session.commit()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch rockets: {e}")
        except ValueError as e:
            raise RuntimeError(f"Error processing rockets response JSON: {e}")
