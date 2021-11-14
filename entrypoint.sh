# git pull
git fetch --all
git pull origin main

echo "Apply database migrations"
python manage.py makemigrations app_collect
python manage.py makemigrations app_expect
python manage.py makemigrations app_manage
python manage.py makemigrations
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
