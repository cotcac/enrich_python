reference:
- https://cumeonet.blogspot.com/2022/08/django-validate-data.html
- https://www.djangoproject.com/
- https://www.django-rest-framework.org/

# Get started
## Create virtual enviroment
```
python -m venv venv
# activate virtual environment
source venv/Scripts/activate

# Install all modules
pip install -r requirements.txt
```

# create a project
django-admin startproject notes
# run server
python manage.py runserver
# create an app
python manage.py startapp topics
python manage.py startapp blogs
```

# Environment variable
```
cp .env.example .env
```

# Migration
```
python manage.py makemigrations
python manage.py migrate
```
# Useful command
```
# Generate requirements.txt
pip freeze > requirements.txt

# Create superuser.
python manage.py createsuperuser
admin/Fpt@12345
```

# Gunicorn
```
gunicorn notes.wsgi
```