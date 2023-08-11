pip install -r requirements.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python3.9 manage.py shell
python3.9 manage.py collectstatic --noinput --clear

