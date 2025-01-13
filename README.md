# tiny-rocket
Dummy app using the SpaceX API

# Requirements

- Docker (and `docker-compose`)
- Python 3
- `pipenv`: To manage the virtual environment, we use `pipenv`. If you do not yet have it, you should first [install it](https://pipenv.pypa.io/en/latest/installation.html).

# Getting started

```bash
# Start the MySQL db in a container
docker compose up -d

# If you need to stop the db
docker compose down

# If you want to clear the db
docker compose down -v
```

# Load all rockets into database

```http request
POST /api/load-rockets
```

# Run the app

```bash
pipenv shell
python -m flask --app application run 

# The app will be available at http://localhost:5000
```