
echo "makemigrations"
python manage.py makemigrations
#python manage.py makemigrations 'app_collect'
#python manage.py makemigrations 'app_expect'
#python manage.py makemigrations 'app_manage'
#python manage.py makemigrations 'app_model'

echo "migrate"
python manage.py migrate

echo "timezone 제거"
python Utils/change_db_datatype.py 'app_collect'

sleep 5m