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

### Add example data (optional)

```
python manage.py shell

from polls.models import Choice, Question
from django.utils import timezone
q = Question(question_text="What's up?", pub_date=timezone.now())
q.save()
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
q.choice_set.create(choice_text='Just hacking again', votes=0)
```

### Start the application

```
python manage.py runserver
```
