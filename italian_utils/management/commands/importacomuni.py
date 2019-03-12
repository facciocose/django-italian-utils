from django.core.management.base import BaseCommand, CommandError
import csv
from django.utils.six import PY3
from italian_utils.models import Comune


class Command(BaseCommand):
    help = "Importa l'elenco dei comuni proveniente dal sito istat"

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'rb') as csvfile:
            csvstring = csvfile.read()
        if PY3:
            import io
            csvfile = io.TextIOWrapper(
                io.BytesIO(csvstring),
                encoding="latin-1"
            )
        else:
            import StringIO
            csvfile = StringIO.StringIO(csvstring)

        comuni_reader = csv.DictReader(csvfile, delimiter=';')
        for row in comuni_reader:
            nome = row['Denominazione (Italiana e straniera)']
            codice_catastale = row['Codice Catastale del comune']
            if nome and codice_catastale:
                c = Comune(nome=nome, codice_catastale=codice_catastale)
                c.save()
        self.stdout.write('Comuni importati correttamente')
