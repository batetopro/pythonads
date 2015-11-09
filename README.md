This projects demonstartes an example
of executed server-side checks of html files,
where on each step the file is first shown in an
iframe and after that a long server check is made.


Requirements:
https://www.python.org/download/releases/2.5/
https://www.djangoproject.com/download/1.3.7/tarball/

Pages:
/ - page showing the queue
/download?url={url} - download a file for the queue

Initialize steps:
1. Go to root folder of the application
2. Type "python2.5 manage.py collectstatic" or "python manage.py collectstatic"

Start: steps:
1. Go to root folder of the application
2. Type "python2.5 manage.py runserver" or "python manage.py runserver"
