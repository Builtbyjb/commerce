dev:
	python manage.py runserver 127.0.0.1:8030

migrate:
	python manage.py makemigrations auctions && python manage.py migrate