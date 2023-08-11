python3.9 manage.py createsuperuser --noinput --username=$DJANGO_SUPERUSER_USERNAME --email=$DJANGO_SUPERUSER_EMAIL --password=$DJANGO_SUPERUSER_PASSWORD
pip install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput --clear

