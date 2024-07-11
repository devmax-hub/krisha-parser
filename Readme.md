### Installation
1. Clone the repo
```sh
git clone git_url
docker-compose build
docker-compose up -d
docker-compose exec -it dj-backend python manage.py migrate
docker-compose exec -it dj-backend python manage.py createsuperuser
```