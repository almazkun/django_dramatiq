run:
	pipenv run python manage.py runserver
dev:
	docker-compose up
prod:
	docker-compose -f docker-compose.prod.yml up -d
down:
	docker-compose down -v
lint:
	pipenv run isort --recursive --force-single-line-imports --line-width 999 .
	pipenv run autoflake --recursive --ignore-init-module-imports --in-place --remove-all-unused-imports .
	pipenv run isort --recursive --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 88 .
	pipenv run black .

add:
	curl -X POST -H "Content-Type: application/json" -d '{"x": 1, "y": 3}' http://localhost
user:
	curl -X POST  http://localhost/user/ \
	-H "Content-Type: application/json" \
	-d '{"username": "test", "password": "nidlaveiuvnb394nvuivnklv", "email": "email@email.com"}'

email:
	curl -X POST  http://localhost/email/ \
	-H "Content-Type: application/json" \
	-d '{"user_id": "1", "email": "email@email.com"}'

users:
	curl http://localhost/users/

list:

migrate:
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate
