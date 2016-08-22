# ToDo Lists

Features:
  - Adding tasks.
  - Modifying existing tasks.
  - Marking complete or incomplete.

Frameworks used:
  - Django==1.4.2
  - Jquery==3.1.0

Running the application:
```sh
$ cd <project_dir>
$ mysql -u root -p < create_user.sql
$ python manage.py syncdb
$ python manage.py runserver
```