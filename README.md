# Medium Scrapper

A Django based web application system, scraping articles from [Article's Official website](https://medium.com/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Clone the repository and open in any code editior, open the terminal and create a fresh virtual environment by typing following command. Then activate it by the next command.

#### On Windows
```python
py -m venv env

.\env\Scripts\activate
```
#### On Mac
```python
python3 -m venv env

cd env

source env/bin/activate
```

### Installing

After successfully activating virtual environment
type the following command to install all requirements for starting the project.

```python
pip install -r requirements.txt
```

At this stage you have successfully done with the installation of project, it is ready to run now with one step remaining i.e., creating database go into `medium_scrapper/settings.py` and check the database name and create the same database in you PostgreSQL application (don't forget to change the password) as mentioned in below code snippet.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medium_scraper', [ create database of same name ]
        'USER': '',  [ posgresql username ]
        'PASSWORD': '', [ Your password ]
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
After configuring your database settings finally run below two commands for making tables required to run the project.

```python
python manage.py makemigrations

python manage.py migrate
```
This will successfully create tables in the database and you can check those tables in you database.
 To run the project type:
 ```python
python manage.py runserver

# then visit below url in your browser:
http://127.0.0.1:8000/
```
And guess what you have successfully configured this system to run on you machine.
