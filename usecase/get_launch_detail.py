import requests


def fetch_all_crew_info():
    response = requests.get('https://api.spacexdata.com/v4/crew')
    return response.json()


def find_crew_info(id, all_crew_info):
    for crew_info in all_crew_info:
        if crew_info["id"] == id:
            return crew_info
    return None


class GetLaunchDetailUsecase:
    @staticmethod
    def execute(launch_id):
        all_crew_info = fetch_all_crew_info()

        response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
        launch = response.json()

        for crew_member in launch["crew"]:
            crew_member["crew"] = find_crew_info(crew_member["crew"], all_crew_info)

        return launch
