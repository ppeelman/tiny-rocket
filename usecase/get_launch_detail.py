import requests


def fetch_all_crew_info():
    try:
        response = requests.get('https://api.spacexdata.com/v4/crew')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch all crew info: {e}")
    except ValueError as e:
        raise RuntimeError(f"Error processing crew response JSON: {e}")


def find_crew_info(crew_id, all_crew_info):
    for crew_info in all_crew_info:
        if crew_info["id"] == crew_id:
            return crew_info
    return None


class GetLaunchDetailUsecase:
    @staticmethod
    def execute(launch_id):
        all_crew_info = fetch_all_crew_info()

        try:
            response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
            response.raise_for_status()
            launch = response.json()

            for crew_member in launch["crew"]:
                crew_member["crew"] = find_crew_info(crew_member["crew"], all_crew_info)

            return launch
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch launch with ID {launch_id}: {e}")
        except ValueError as e:
            raise RuntimeError(f"Error processing launch with id {launch_id} response JSON: {e}")
