import requests


class FetchAllLaunchesUsecase:
    @staticmethod
    def execute(page):
        options = {"options": {"limit": 5, "page": page or 1}}
        response = requests.post('https://api.spacexdata.com/v5/launches/query', json=options)
        return response.json()
