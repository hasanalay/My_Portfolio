pip install -r requirements.txt
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python3 manage.py shell
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput --clear

