# explaining pizza_pys

I'm trying a few things out here. I initially though I wanted to get going with this project in flask, but I found a tutorial to build a docker environment with flask. 
There is some code in here that started this idea so it might look a little messy for a while. But it can keep living here for now.

I removed these from requirements.txt 
Click==7.0
Flask==1.1.1
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
SQLAlchemy==1.3.11
Werkzeug==0.16.0

##### Docker Tut for this project

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

##### Postgres

http://initd.org/psycopg/docs/install.html


There are some requirements around the adapter being used for postgres, I'll use the wheel package for now but the doc does say this. 
`For production use you are advised to use the source distribution.`


##### Limitation for psycopg
One of the requirements for psycopg is libpq-dev, it has minimal binaries and headers for Postgresql. This was listed on the pypl site for libpq-dev 

```
Currently ``libpq-dev`` is being built only for ``Linux`` with
``Python 2.7, 3.3, 3.4`` from `PostgreSQL 9.*` sources.
```

For now I will try installing these headers in the image.


##### Running Development 

 docker-compose up -d --build
 docker-compose exec pys python manage.py migrate --noinput `this doesn't need to be run with an entrypoint`

*verify the volume*
 docker volume inspect pizza-for-the-win_postgres_data

*verify postgres migrations were run*
 docker-compose exec pizza-for-the-win_db_1 psql --username=hello_django --dbname=hello_django_dev