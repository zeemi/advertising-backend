# advertising-backend

## tech-stack
Application has been written in python3 using Django==2.1 and djangorestframework==3.8.2.

to start project locally:
- prepare one of two environments listed below:
  - create `local.py` settings from local.py.tmp template

- create python3 virtual environment and use it in all next steps
- install `requirements.txt`
- perform db migrations and remember to use proper settings:  python manage.py migrate  --settings=api.settings.<local/prod>
- start server: python manage.py runserver  --settings=api.settings.<local/prod>


## concept
- returning data to frontend and keeping metrics up to date in local database is done independently
- by design, server should be running periodically management command: `load_metrics` . Simplest scheduling could be done by `cron`, ex once per hour
- there is a big room for improvements - direction should be chosen after knowing more about business case and policy of data updates
- some of possible improvements:
    - applying indexes
    - aggregate data returned to frontend when timespan is big enough
    - load csv in chunks
    - batching database updates
