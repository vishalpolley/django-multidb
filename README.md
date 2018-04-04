# Django Multiple Database Connectivity
Configuring Multiple Databases in Django.

**Databases**

The project Postgresql and MySQL as backend databases.

### Postgresql database setup
The data of the fisrt app is being saved in the postgresql database. The default database is 'form', which can be easily changed through the `settings.py` file.

#### Configuring Postgres Installation
* After installing postgresql database, open psql by running the following commands
```
sudo -u postgres psql postgres
```
* Set up password for the default `postgres` user
```
\password postgres
```
* Enter the password
* Quit psql
```
\q
```
#### Creation of databases in Postgresql
* For creating the database, open psql by executing the following commands
```
sudo -u postgres psql
```
* Now create a new database named as `form`
```
postgres=# createdb form;
```
* The default database setup for Postgresql for app1 in `settings.py` file are as follows :-
```
'form1_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'form',
        'USER': 'enter postgres username', # Default is postgres
        'PASSWORD': 'enter postgres password',
        'HOST': 'localhost',
        'PORT': '',
    },
```

### MySQL database setup
The data of the second app is being saved in the MySQL database. The default database is 'form', which can be easily changed through the settings.py file.
* After installing MySQL, open it by running the command
```
mysql -u root
```
* Now create a database named as `form`
```
CREATE DATABASE form;
```
* The default database setup for MySQL for app2 in `settings.py` file are as follows :-
```
'form2_db': {
        'NAME': 'form',
        'ENGINE': 'django.db.backends.mysql',
        'HOSTNAME': 'localhost',
        'USER': 'enter mysql username', # Default is root
        'PASSWORD': 'enter mysql password', 
        'OPTIONS': {
                'autocommit': True,
        },
    },
```

## Setting Up the Project
* Firstly clone/download the repo [here](https://github.com/vishalpolley/django-multidb/archive/master.zip)
```
git clone https://github.com/vishalpolley/django-multidb.git
```
* Navigate inside the multidb folder
```
cd multidb/
```
* Install all the dependencies required for the project
```
pip install -r requirements.txt
```
* The default credentials for super user are 
```
username: user
password: qwerty123
```
* Run the migrations for the postgresql database for app1
```
python manage.py migrate --database=form1_db
```
* Run the migrations for the mysql database for app2
```
python manage.py migrate --database=form2_db
```
* Now run the server by using
```
python manage.py runserver
```
* Enter the following URL to navigate to the first app
```
http://127.0.0.1:8000/app1/
```
* Enter the following URL to navigate to the first app
```
http://127.0.0.1:8000/app2/
```
* Check the database enteries on Django admin
```
http://127.0.0.1:8000/admin/
```
enter the default credentials to login to the Django admin

#### Checking the entries over individual databases

**Postgresql**

The database enties for the App1 are stored in `app1_form1` table
* To fetch the entries from the table, execute the following query over psql
```
form=# select * from app1_form1;
```
You get the entries in the following format
```
 id | first_name | last_name 
----+------------+-----------
  4 | Vishal     | Polley
(1 row)
```

**MySQL**

The database enties for the App2 are stored in `app2_form2` table
* To fetch the entries from the table, execute the following query over mysql cli
```
MariaDB [form]> select * from app2_form2;
```
You get the entries in the following format
```
+----+-------------+-------------+
| id | father_name | mother_name |
+----+-------------+-------------+
|  4 | Vishwajeet  | Shyamali    |
+----+-------------+-------------+
1 row in set (0.00 sec)
```
