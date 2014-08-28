# django-italian-utils

[![Build Status](https://travis-ci.org/facciocose/django-italian-utils.svg?branch=master)](https://travis-ci.org/facciocose/django-italian-utils) [![Coverage Status](https://img.shields.io/coveralls/facciocose/django-italian-utils.svg)](https://coveralls.io/r/facciocose/django-italian-utils?branch=master)

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

Effettuare le migrazioni (attualmente compatibili solo con django <=1.7)

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

Un dizionario delle [regioni e le relative province con abbreviazioni annesse](https://github.com/facciocose/django-italian-utils/blob/master/italian_utils/utils.py).

### Elenco dei comuni

È possibile importare il file zip con l'[elenco dei comuni proveniente dal sito istat](http://www.istat.it/it/archivio/comuni) con un comando manage.py

`python manage.py importacomuni <file_zip>

## TODO

- Aggiornare la validazione del CF per includere i casi di omocodia
- Creare le tuple da usare nei ChoiceField
- Mappare i modelli di comuni, province e regioni tramite i codici istat