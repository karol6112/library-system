# Library management system
> This app allow to manage library. It consist of two parts. The first part is "User" app where we can register and log in to the account. The second is "Book" app where we can add books to the system. Each book is assigned to the author and category. The application can filter and search data. "Book" app has also two functions "borrow" and "back" which allow to borrow book and return it.

## Table of contents
* [Requirements](#requirements)
* [Install](#install)
* [Connect to database](#connect_to)

## Requirements
* Python3
* PostgreSQL

## Connect to database
* Set up local_settngs.py from local_settings.template. 
* In file add data necessary to connect to PostgreSQL database.

## Install 
* Create virtual environment and activate it
```
$: virtualenv venv
$: source venv/bin/activate
```

* Clone git repository
```
$: git clone https://github.com/karol6112/library-system.git
```

* Install requirements
```
$: pip install -r requirements.txt
```

* Make migrations
```
$: python manage.py makemigrations
```

* In file add data necessary to connect to PostgreSQL database.
