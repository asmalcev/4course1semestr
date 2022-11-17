```
mkdir app && cd app
python3.8 -m venv env
source env/bin/activate

pip install django==3.2.6
django-admin startproject dockercase .

python manage.py migrate
python manage.py runserver

pip freeze > requirements.txt

touch Dockerfile

cd ..
touch docker-compose.yml

touch .env.dev

docker-compose build
docker-compose up -d
```