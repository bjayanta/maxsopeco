# MaxSOP Eco System
Simple eco system for MaxSOP. To-Do, Daily expense, Note etc is some basic features. 

## Installation

### Step 1:
Install & create virtual environment 
> pip install virtualenv

> pip -m venv \<env-name>

### Step 2:
Activate virtual environment (Windows)
> cd \<env-name>\Scripts\

> activate

### Step 3:
Install Django
> pip install django

### Step 4:
Install [MySQL Client](https://pypi.org/project/mysqlclient/)
> pip install mysqlclient 

### Step 5:
Serve the server.
> python manage.py runserver 

or, 
> python manage.py runserver \<ip-address>:\<port-number>

Do not forgot to update "ALLOWED_HOSTS" from project settings.

### Step 6:
Make migrations & migrate to database 
> python manage.py makemigrations

> python manage.py migrate

### Step 7:
Create superadmin
> python manage.py createsuperuser 

# Step 8:
Generate dependance list
> pip freeze > requirements.txt

Install dependance recursively
> pip install -r .\requirements.txt

