echo "Build Started"
python -m pip install requirements.txt
python manage.py collectstatic --noinput --clear