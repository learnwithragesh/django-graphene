Create a Virtual Environment: python -m venv venv_path
To Activate a Virtual Environment: source venv_path/bin/activate

Install DJANGO and GraphQL Packages: pip install django graphene-django django-filter django-graphql-jwt

Create Project: django-admin startproject project_name
cd project_name

To Migrate: python manage.py migrate (Run migration to make the model changes work)
To Run Server: python manage.py runserver

To Configure: 
1. Add 'graphene_django' in Installed_apps under project_name/settings.py
2. Add GRAPHENE = { 'SCHEMA': 'app_name.schema.schema', } to last in project_name/settings.py 

To start new app: python manage.py startapp app_name
To edit the models in app: use app_name/models.py
Add the app to Installed_apps

Create the database tables: 
python manage.py makemigrations
python manage.py migrate