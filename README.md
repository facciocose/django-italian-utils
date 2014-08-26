django-italian-utils
====================

Libreria di utility per semplificare la creazione di applicazioni italiane

Attualmente sono presenti dei validatori per **codice fiscale** e **partita iva** da usare nei modelli.
```python
class Persona(InformazioniBase):
    codice_fiscale = models.CharField(
        max_length=16,
        validators=[validate_codice_fiscale]
    )

    # ...

class Azienda(InformazioniBase):
    partita_iva = models.CharField(
        max_length=11,
        validators=[validate_partita_iva]
    )

    # ...
```
