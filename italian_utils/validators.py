from django.core.exceptions import ValidationError
import re
import string


def validate_codice_fiscale(value):
    codice_fiscale_re = re.compile(
        r'^[a-zA-Z]{6}\d{2}[a-zA-Z]\d{2}[a-zA-Z]\d{3}[a-zA-Z]'
    )

    if not codice_fiscale_re.match(value):
        raise ValidationError('Inserisci un codice fiscale formalmente valido')

    conversione_pari = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25,
    }

    conversione_dispari = {
        '0': 1,
        '1': 0,
        '2': 5,
        '3': 7,
        '4': 9,
        '5': 13,
        '6': 15,
        '7': 17,
        '8': 19,
        '9': 21,
        'A': 1,
        'B': 0,
        'C': 5,
        'D': 7,
        'E': 9,
        'F': 13,
        'G': 15,
        'H': 17,
        'I': 19,
        'J': 21,
        'K': 2,
        'L': 4,
        'M': 18,
        'N': 20,
        'O': 11,
        'P': 3,
        'Q': 6,
        'R': 8,
        'S': 12,
        'T': 14,
        'U': 16,
        'V': 10,
        'W': 22,
        'X': 25,
        'Y': 24,
        'Z': 23,
    }

    conversione_controllo = dict(enumerate(string.ascii_uppercase))

    pari, dispari = [], []

    for i, x in enumerate(value[:-1].upper()):
        if i % 2 == 0:
            dispari.append(x)
        else:
            pari.append(x)

    valore_controllo = sum(
        [conversione_pari[x] for x in pari] +
        [conversione_dispari[x] for x in dispari]
    ) % 26

    carattere_controllo = conversione_controllo[valore_controllo]

    if carattere_controllo != value[-1].upper():
        raise ValidationError('Inserisci un codice fiscale formalmente valido')


def validate_partita_iva(value):
    partita_iva_re = re.compile(
        r'^\d{11}'
    )

    if not partita_iva_re.match(value):
        raise ValidationError('Inserisci una partita iva valida')

    pari, dispari = [], []

    for i, x in enumerate(value):
        if i % 2 == 0:
            dispari.append(int(x))
        else:
            pari.append(int(x))

    controllo = (sum(pari) + sum(dispari)) % 10
    if controllo != 0:
        raise ValidationError('Inserisci una partita iva valida')
