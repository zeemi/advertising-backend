# advertising-backend

application has been written in python3 using Django==2.1 and djangorestframework==3.8.2.

to start project locally:
- prepare one of two environments listed below:
  - create `local.py` settings from local.py.tmp template

- create python3 virtual environment and use it in all next steps
- install `requirements.txt`
- perform db migrations and remember to use proper settings:  python manage.py migrate  --settings=api.settings.<local/prod>
- start server: python manage.py runserver  --settings=api.settings.<local/prod>