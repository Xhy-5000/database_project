Database_project
====
A student manage system base on django and mysql.
This project is done by five students in CUHKSZ.
## Installation

Python and Django need to be installed

```bash
pip install django
pip install pymysql
```

## Usage

Go to the database_project folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for students and teachers.  
The username is their name and password for everyone is 'csc3170'.  

Example usernames:  
student- 'Andy Xia'  


```bash
python manage.py createsuperuser
```
