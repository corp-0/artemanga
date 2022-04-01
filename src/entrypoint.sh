#!/bin/sh

if [ -n "$DB_NAME" ] && [ "$DB_NAME" = "postgres" ]
then
    echo "Esperando a postgres..."

    if [ -z "$DB_HOST" ]
    then host="db"
    else host="$DB_HOST"
    fi

    if [ -z "$DB_PORT" ]
    then port="5432"
    else port="$DB_PORT"
    fi

    while ! nc -z $host $port; do
        sleep 0.1
    done

    echo "Base de datos inicializada"
fi

# elimina datos en la base de datos
#python manage.py flush --no-input

python manage.py makemigrations --noinput
python manage.py migrate --noinput

# busca estáticos y los copia a la carpeta de producción
python manage.py collectstatic --no-input

exec "$@"