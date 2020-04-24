# django-italian-utils

[![Build Status](https://travis-ci.org/facciocose/django-italian-utils.svg?branch=master)](https://travis-ci.org/facciocose/django-italian-utils) [![Coverage Status](https://coveralls.io/repos/github/facciocose/django-italian-utils/badge.svg?branch=master)](https://coveralls.io/github/facciocose/django-italian-utils?branch=master)

Utility library which simplifies the creation of Italian applications

[Italian README](README.it.md)

## Install

Use pypi to install the package

`pip install django-italian-utils`

Add `italian_utils` to installed apps

```python
#...

INSTALLED_APPS = (
    # ...
    'italian_utils',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# ...
```

Run migrations

`python manage.py migrate`

## Contents

Validators for **codice fiscale** and **partita iva** inside your models.
```python
from italian_utils.validators import validate_codice_fiscale, validate_partita_iva

class Persona(models.Model):
    codice_fiscale = models.CharField(
        max_length=16,
        validators=[validate_codice_fiscale]
    )

    # ...

class Azienda(models.Model):
    partita_iva = models.CharField(
        max_length=11,
        validators=[validate_partita_iva]
    )

    # ...
```

A dictionary of Italian [region and provinces with abbreviations](italian_utils/utils.py).

### City list

You can import the CSV file containing the [list of cities provided by istat](https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv) with a manage.py command

`python manage.py importacomuni <file_csv>`

## TODO

- Link models of cities, provinces and regions using istat codes
