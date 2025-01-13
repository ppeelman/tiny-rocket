from db.models.rocket import Rocket
from usecase.load_rockets_from_api import LoadRocketsFromApiUsecase


class GetAllRocketsUsecase:
    @staticmethod
    def execute():
        rockets = Rocket.query.all()

        if len(rockets) == 0:
            LoadRocketsFromApiUsecase.execute()

        return Rocket.query.all()
