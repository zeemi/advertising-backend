# advertising-backend

## Tech-stack
Application has been written in python3 using Django==2.1 and djangorestframework==3.8.2.

## Instruction to start locally
- create `local.py` settings from local.py.tmp template
- create python3 virtual environment and use it in all next steps
- install `requirements.txt`
- perform db migrations and remember to use proper settings:  `python manage.py migrate  --settings=api.settings.local`
- start server: `python manage.py runserver  --settings=api.settings.local`
- schedule by cron or run manually: `python manage.py load_metrics --settings=api.settings.local`


## Concept
- analyzing/fetching raw metrics and returning prepared metrics to frontend are done independently
- management command `load_metrics` should be run periodically on server. Simplest scheduling could be done by `cron` - for example once per hour
- NOTE: this solution is not optimised in any way, but some of possible options are proposed in next step. Actual improvement should be chosen after knowing more about business case and policy of data updates

## Suggested improvements:
- apply indexes on `Metric` table
- analyse if loading data finishes in acceptable time - hard deadline: it has to finish before next run, otherwise:
    - batch database updates
    - chunk and load csv partially if size can be a problem
    - alternatively - load csv directly using database engine
- add caching
- update django version
