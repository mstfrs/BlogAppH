

web: gunicorn main.wsgi:application --log-file - --log-level debug
web: python manage.py runserver 0.0.0.0:$PORT
python manage.py collectstatic --noinput
heroku ps:scale web=1
manage.py migrate
