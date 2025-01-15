import requests


class FetchAllLaunchesUsecase:
    API_URL = "https://api.spacexdata.com/v5/launches/query"

    @staticmethod
    def execute(page=1):
        options = {"options": {"limit": 5, "page": page or 1}}

        try:
            response = requests.post(FetchAllLaunchesUsecase.API_URL, json=options)
            response.raise_for_status()
            launches = response.json()

            # Filter launches with crew (also set limit to a very high number)
            # launches["docs"] = [launch for launch in launches.get("docs", []) if launch.get("crew")]

            return launches
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch launches: {e}")
        except ValueError as e:
            raise RuntimeError(f"Error processing launch response JSON: {e}")
