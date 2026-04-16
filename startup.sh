#!/bin/bash
echo "Running Django migrations..."
python manage.py migrate --noinput
echo "Setting gabeitch password..."
python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); u=U.objects.get(username='gabeitch'); u.set_password('GameRanking@2026!'); u.save(); print('PASSWORD SET OK')"
echo "Starting gunicorn..."
gunicorn Game_Ranking.wsgi:application --bind 0.0.0.0:8000
