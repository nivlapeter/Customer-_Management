serve:
	python3 manage.py runserver
superuser:
	python3 manage.py createsuperuser
migrate:
	python3 manage.py migrate
app:
	django-admin startapp $(name)	 
migrations:
	python3 manage.py makemigrations $(app)
check:
	python3 manage.oy check
collectstatic:
	python manage ,py collectstatic	
test:
	python3 manage.py test $(app)
shell:
	python3 manage.py shell 
check:
	python3 manage.py check
