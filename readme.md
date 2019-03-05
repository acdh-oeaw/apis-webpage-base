# About
[APIS](https://acdh-oeaw.github.io/apis-core/) is a [Django](https://www.djangoproject.com/) based webapplication developed by the [Austrian Centre for Digital Humanities](https://acdh.oeaw.ac.at/). We use it to store named entities and relations between them in DH projects.



This is a base project for [APIS](https://acdh-oeaw.github.io/apis-core/) installations. We use different branches to adapt the base project to the needs of the various projects

# Basic Installation
* Clone this repository and checkout the branch you intend to use
* Create a virtualenv and activate it: 

    ```bash
    virtualenv -p python3 myenv
    source myenv/bin/activate
    ```

* Install the requirements: 

    ```bash
    pip install -r requirements.txt
    ```

* Migrate the database:

    ```bash
    python manage.py migrate
    ```

* Add apis-core to urls.py:

    ```bash
    vim ROOT_OF_APIS/apis/urls.py
    ```
    uncomment line #8 and save the file
* Migrate again:
    
    ```bash
    python manage.py makemigrations browsing
    python manage.py migrate
    ```

* and run the development server:

    ```bash
    python manage.py runserver
    ```

# Installation for production
For security and performance reasons you dont want to use the development server and/or sqllite.

## Use mysql instead of sqllite

* change to ROOT_OF_APIS/apis/settings
* copy dev.py to server.py
* change the DATABASES entry to something along the lines of:

    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE NAME',
        'USER': 'MYSQL USER',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

* install the myqlclient library to your virtualenv:

    ```bash
    pip install mysqlclient
    ```

## Use apache2 instead of the development server

* for installing and configuring apache2 refer to instructions of your system
* an example virtualhost definition file:

# Additional packages
We have developed (and still are developing) some additional packages to extend the functionalities of APIS.

## Highlighter
This package is used to provide annotation functionalities for texts stored in APIS. If installed and 

# References

* Introduction to the system: [Schlögl, M., & Lejtovicz, K. (2018). A Prosopographical Information System (APIS)](http://ceur-ws.org/Vol-2119/paper9.pdf) In Proceedings of the Second Conference on Biographical Data in a Digital World 2017 (S. 6). CEUR Workshop Proceedings.
