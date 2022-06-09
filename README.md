# InstaClone


#### By Joylene Kirui

# Description
InstaClone is a clone of the website for the popular photo app Instagram

# Features
- User can sign in to the application to start using.
- Users are able to upload their pictures to the application.
- Users can see their profile with all their pictures.
- One can follow other users and see their pictures on my timeline.
- Users can like a picture and leave a comment on it.
# Live link
https://myinstaclone.herokuapp.com/

# Requirements
The InstaClone project requires a prerequisite understanding of the following:

- Django Framework

- Python3.8

- Postgres

- Python virtualenv

# Setup and Installation
##### Clone repo (git clone https://github.com/JoyleneKirui/insta-clone.git)

####  Create and Activate virtual environment
-python3 -m venv virtual

-source virtual/bin/activate

#### Install dependancies
Install dependancies that will create an environment for the app to run pip install -r requirements.txt

#### Create the Database
- psql

- CREATE DATABASE insta-clone;

#### Run initial Migration
python3 manage.py makemigrations gallery

python3 manage.py migrate

#### Run the app
python3 manage.py runserver

Open terminal on localhost:8000

## Known bugs
No known bugs so far.

## Technologies Used
- Python 3.8

- Django MVC framework

- HTML, CSS and Bootstrap

- JavaScript

- Postgressql

- Heroku

##  License
Copyright (c) [2022] [Joylene Kirui]
[MIT License](https://choosealicense.com/licenses/mit/)