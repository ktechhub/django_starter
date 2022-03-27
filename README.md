# django_starter
A django boiler template to start your project with configuration out of the box

This is just the template version.

## Clone the Project
```sh
git clone git@github.com:ktechhub/django_starter.git
```

## Copy the .env file and update the values
```sh
cp .env.example .env
```

## Run with Docker
To run with docker, set CONTAINER_STATUS in your .env
```.env
CONTAINER_STATUS=True
```

### Run docker compose

```sh
docker-compose up --build
```

### Running into issues?
```sh
sudo docker-compose up --build
```


## Running project on local machine

### Create Virtualenv and Install requirements
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Run Server
```sh
python manage.py runserver
```


## Contributing / Pushing to GitHub
Checkout to your branch before working

Always pull from the main branch to stay in sync

After you are done and you want to push to github, run the command below:

`make sure the environment is activated`

```sh
python git_push.py
```

`make sure the virtual environment is activated`

Follow the prompts to push to your branch

After that make a pull request to main branch and request for a review. It will be reviewed and merged if there no conflicts.

