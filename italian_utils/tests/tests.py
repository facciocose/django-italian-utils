from django.test import TestCase
from django.core.exceptions import ValidationError
from italian_utils.validators import validate_codice_fiscale
from italian_utils.validators import validate_partita_iva
from italian_utils.utils import REGIONI
from italian_utils.models import Comune


class ValidateCodiceFiscaleTestCase(TestCase):
    def test_codice_fiscale_vuoto(self):
        self.assertRaises(
            ValidationError,
            validate_codice_fiscale,
            ''
        )

    def test_codice_fiscale_16(self):
        self.assertRaises(
            ValidationError,
            validate_codice_fiscale,
            '1234567890123456'
        )

    def test_codice_fiscale_controllo(self):
        self.assertRaises(
            ValidationError,
            validate_codice_fiscale,
            'ABCDEF00A00A000A'
        )

    def test_codice_fiscale_formalmente_corretto(self):
        self.assertEqual(validate_codice_fiscale('RSSMRA14M26H501N'), None)


class ValidatePartitaIva(TestCase):
    def test_partita_iva_vuota(self):
        self.assertRaises(
            ValidationError,
            validate_partita_iva,
            ''
        )

    def test_partita_iva_non_numerica(self):
        self.assertRaises(
            ValidationError,
            validate_partita_iva,
            'ABC123DEF45'
        )

    def test_partita_iva_controllo(self):
        self.assertRaises(
            ValidationError,
            validate_partita_iva,
            '12345678901'
        )

    def test_partita_iva_formalmente_corretta(self):
        self.assertEqual(validate_partita_iva('12345678905'), None)


class ValidateRegioni(TestCase):
    def test_numero_regioni(self):
        self.assertEqual(len(REGIONI), 20)

    def test_roma_in_lazio(self):
        self.assertTrue(
            any(['Roma' in comune['nome'] for comune in REGIONI['Lazio']])
        )


class ValidateComuni(TestCase):
    def test_crea_comune(self):
        comune = Comune(nome='Catania', codice_catastale='C351')
        self.assertEqual(str(comune), 'C351: Catania')
