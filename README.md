# Project to learn Django with Platzi

## Requirements

To run this project you will need have installed

- Docker
- Docker-compose

## Instructions to run

Run into terminal the next command to get running the project into port 8000

``` sh
docker-compose run
```

## Create new project

You can create a new project from `Dockerfile`, `docker-compose.yml` and `requirements.txt`, just by using

``` sh
docker-compose run web django-admin startproject <project_name> .
```
This will create an entire django project here FROM the container

## Access to creation commands

You can perform activities like `createsuperuser`, `makemigrations` or `migrate` from the `manage.py` file by using this command

``` sh
# If container is running
docker-compose exec web <command>

# Example
docker-compose exec web python manage.py makemigrations
```

If you're not running the docker-compose project in the moment, just change, you can use of this command

``` bash
docker-compose run web <command>
```

Just like the before one, but changing 'exec' with 'run' and adding the --rm flag to delete container on finish