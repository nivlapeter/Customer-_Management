# Customer Management
#### management app

## Description


## Link to deployed site



## Set Up and Installations

### Prerequisites
1. Ubuntu Software (20.04)
2. Python3.8
3. [Postgres](https://www.postgresql.org/download/)
4. python virtualenvironment
5. Django-Restframework

### Clone the Repo
Run the following command in your terminal:
`git clone {the Customer Management repository}

### Activate virtual environment
Activate virtual environment using python3.8 as default handler
```bash
virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE  ;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DB_NAME = '<db_name>'
DB_USER = '<db_user>'
DB_PASSWORD = '<db_password>'
DEBUG = True
ALLOWED_HOSTS='*'
CLOUD_NAME='<cloudinary_name>'
API_KEY='<cloudinary_api_key>'
API_SECRET='<cloudinary_secret>'
EMAIL_USE_TLS='True'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='<email address>'
EMAIL_HOST_PASSWORD='<password>'

run the (source .env) command in your terminal to update the .env file

```
### Run initial Migration
```bash
python3.8 manage.py makemigrations 
python3.8 manage.py migrate
```

### Run the app
```bash
python3.8 manage.py runserver
```
Open terminal on `localhost:8000`

## Technologies used
    - Python 3.8
    - Django 3
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django_Rest_framework

## Support and contact details
Contact me for further help/support through my github handle

### License
MIT Copyright (c) 2020
