[source](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx python3.8-venv
```

```
sudo -u postgres psql

create database casedb;
create user caseuser with encrypted password 'caseuserpass';

ALTER ROLE caseuser SET client_encoding TO 'utf8';
ALTER ROLE caseuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE caseuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE casedb TO caseuser;
```

```
mkdir django_project
python3 -m venv caseenv
source caseenv/bin/activate

pip install django gunicorn psycopg2-binary
django-admin startproject caseproj

vim caseproj/caseproj/settings.py
```

```
ALLOWED_HOSTS = ['*']
```

```
DATABASES = {
		'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': 'casedb',
				'USER': 'caseuser',
				'PASSWORD': 'caseuserpass',
				'HOST': 'localhost',
				'PORT': '',
		}
}
```

```
import os
...
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

```
cd ../
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
[username=supercaseuser]
[password=supercaseuserpass]

python manage.py collectstatic
```

```
sudo ufw allow 8000
python manage.py runserver 0.0.0.0:8000

gunicorn --bind 0.0.0.0:8000 caseproj.wsgi
```

```
sudo vim /etc/systemd/system/gunicorn.service
```
```apache
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/django_project/caseproj
ExecStart=/django_project/caseenv//bin/gunicorn --access-logfile - --workers 3 --bind unix:/django_project/caseproj/caseproj.sock caseproj.wsgi:application

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl status gunicorn

sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

```
sudo vim /etc/nginx/sites-available/caseproj
```
```nginx
server {
	listen 80;
	server_name server_ip;

	location /static/ {
		root /django_project/caseproj/static;
	}

	location / {
		include proxy_params;
		proxy_pass http://unix:/django_project/caseproj/caseproj.sock;
	}
}
```
```
sudo ln -s /etc/nginx/sites-available/caseproj /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```
```
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```