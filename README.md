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

## Initialize Database

1. Open your mysql work bench and run init_db.sql
2. Find the settings.py in mysite dictionary, change the mysql username and password into yours'
![code_image](./polls/images/1.png)

## Usage

Go to the database_project folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for students and teachers.  
The username is their name and password for everyone is 'csc3170'.  

#### Example usernames:  
student
> * Andy Xia
> * Dodo Xia
> * Alex Li
> * Arthur Li

teacher
> * Donald Trump
> * Borris Johnson

