# django-italian-utils

[![Build Status](https://travis-ci.org/facciocose/django-italian-utils.svg?branch=master)](https://travis-ci.org/facciocose/django-italian-utils) [![Coverage Status](https://img.shields.io/coveralls/facciocose/django-italian-utils.svg)](https://coveralls.io/r/facciocose/django-italian-utils?branch=master)

Libreria di utility per semplificare la creazione di applicazioni italiane

## Installazione

`pip install django-italian-utils`

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

## TODO

- Aggiungere l'elenco aggiornato dei comuni italiani (riferimento: http://www.istat.it/it/archivio/comuni) da usare nei `ChoiceField`