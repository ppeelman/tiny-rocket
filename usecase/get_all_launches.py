import requests


class FetchAllLaunchesUsecase:
    API_URL = "https://api.spacexdata.com/v5/launches/query"

    @staticmethod
    def execute(page=1):
        if not isinstance(page, int) or page < 1:
            raise ValueError("Page must be a positive integer.")

        options = {"options": {"limit": 5000, "page": page or 1}}

        try:
            response = requests.post(FetchAllLaunchesUsecase.API_URL, json=options)
            response.raise_for_status()
            launches = response.json()

            # Filter launches with crew
            launches["docs"] = [launch for launch in launches.get("docs", []) if launch.get("crew")]

            return launches
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch launches: {e}")
        except ValueError as e:
            raise RuntimeError(f"Error processing launch response JSON: {e}")
