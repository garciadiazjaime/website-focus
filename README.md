Focus Website
====

[![Build Status](https://travis-ci.org/garciadiazjaime/website-focus.svg)](https://travis-ci.org/garciadiazjaime/website-focus)


Technologies:
django


Package Installation
`pip install -r requirements.txt`

Run Server
`cd project`
`python manage.py runserver`

GUI - Admin
http://127.0.0.1:8000/admin

DB Setup
`psql -c create database focus -U postgres`
`python manage.py migrate`
`python manage.py createsuperuser` (this is the user for access the admin, feel free to type anything)
`python manage.py loaddata data/fixtures/data.json`
`python manage.py loaddata data/survey/data.json`

Drop Database
`psql -c drop database focus`

Deploy project
`fab update`
`git status`
`git diff`
`fab deploy`

sprites
`npm run sprites`

## mirror website
wget --mirror --convert-links --adjust-extension --page-requisites
wget -mkEpnp http://127.0.0.1:8000/

## Docker commands
`docker build -t garciadiazjaime/website-focus . --platform linux/amd64`
`docker run -d -p 49169:8000 garciadiazjaime/website-focus`
`docker push garciadiazjaime/website-focus`
`docker pull garciadiazjaime/website-focus`
