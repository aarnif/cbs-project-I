# cbs-project-I

Cyber Security Base 2025 Course Project I

## How to run the application:

### Clone the repository

```
HTTPS - git clone https://github.com/aarnif/cbs-project-I.git

SSH - git clone git@github.com:aarnif/cbs-project-I.git
```

### Set up virtual environment

```
cd cbs-project-I

python -m venv venv

source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Set up database

```
cd mysite

python manage.py makemigrations

python manage.py migrate
```

### Start the application

```
python manage.py runserver
```
