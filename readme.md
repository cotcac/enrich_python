reference:
- https://cumeonet.blogspot.com/2022/08/django-validate-data.html
- https://www.djangoproject.com/
- https://www.django-rest-framework.org/

# Get started
Install django
```
python -m pip install Django
python -m django --version

# create a project
django-admin startproject notes
# run server
python manage.py runserver
# create an app
python manage.py startapp topics
python manage.py startapp blogs
```

# Migration
```
python manage.py makemigrations
python manage.py migrate
```