# Offer manager

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Backenv realization offer manager

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```
git clone https://github.com/tenatarika/AI_site.git
```

```
cd offermanager
```

Now need to install Pipenv to install dependencies
```
pip install pipenv 
```

create virtual env
```
pipenv shell
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pipenv install
```

create migrations
```
python manage.py makemigrations 
```

complite migrations
```
python manage.py migrate
```


End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Create superuser

```
python manage.py createsuperuser
```

Run server
```
python manage.py runserver
```
