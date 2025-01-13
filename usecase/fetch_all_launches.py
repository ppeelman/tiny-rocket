import requests


def fetch_all_crew_info():
    response = requests.get('https://api.spacexdata.com/v4/crew')
    return response.json()


def find_crew_info(id, all_crew_info):
    for crew_info in all_crew_info:
        if crew_info["id"] == id:
            return crew_info
    return None


class FetchAllLaunchesUsecase:
    @staticmethod
    def execute(page):
        all_crew_info = fetch_all_crew_info()

        options = {"options": {"limit": 5, "page": page or 1}}
        response = requests.post('https://api.spacexdata.com/v5/launches/query', json=options)
        launches = response.json()

        for launch in launches["docs"]:
            if len(launch["crew"]) != 0:
                for crew_member in launch["crew"]:
                    crew_member["crew"] = find_crew_info(crew_member["crew"], all_crew_info)

        return launches
