# django-italian-utils

[![Build Status](https://travis-ci.org/facciocose/django-italian-utils.svg?branch=master)](https://travis-ci.org/facciocose/django-italian-utils) [![Coverage Status](https://coveralls.io/repos/github/facciocose/django-italian-utils/badge.svg?branch=master)](https://coveralls.io/github/facciocose/django-italian-utils?branch=master)

Libreria di utility per semplificare la creazione di applicazioni italiane

## Installazione

Installare il pacchetto pypi

`pip install django-italian-utils`

Aggiungere `italian_utils` alle app installate

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

Effettuare le migrazioni

`python manage.py migrate`

## Contenuto

Sono presenti dei validatori per **codice fiscale** e **partita iva** da usare nei modelli.
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

Un dizionario delle [regioni e le relative province con abbreviazioni annesse](italian_utils/utils.py).

### Elenco dei comuni

È possibile importare il file CSV con l'[elenco dei comuni proveniente dal sito istat](https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv) con un comando manage.py

`python manage.py importacomuni <file_csv>`

## TODO

- Mappare i modelli di comuni, province e regioni tramite i codici istat
