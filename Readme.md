Being in senior year, we were looking for internships. After giving a few tests, we figured there might be a way to find applicants whose personality type and values match with the company. We developed

1. A full-stack CRM software in Django
2. [A personality prediction ML API in Flask](https://github.com/kakabisht/Predicting-personality-from-text-using-AI)
3. [A sentiment prediction DL API in Flask](https://github.com/kavy9/emotion-prediction-api)

### How to run this application

1. Create a virtual enviornment
2. pip install -r requirements.txt (to install all required libraries)
3. cd applicant_filter
4. python manage.py runserver

### If an error occurs regarding the data base,delete all **pycache** , migrations from all folders along with the db. Then run the following commands,

1. python manage.py migrate
2. python manage.py makemigrations
3. python manage.py migrate

### How to create a admin in our application,

1. python manage.py createsuperuser
2. python manage.py runserver

### for more information on django: https://programmerprodigy.code.blog/2020/07/09/basics-of-django-framework/

### for more information on our topic, read our paper:
