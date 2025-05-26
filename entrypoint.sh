#!/bin/sh

set -e

echo "Waiting for database $SQL_HOST:$SQL_PORT"
until pg_isready -h "$SQL_HOST" -p "$SQL_PORT" > /dev/null 2>&1; do
  sleep 0.5
done

echo "Applying migrations"
python manage.py migrate --noinput

echo "Collecting static"
python manage.py collectstatic --noinput

exec "$@"
