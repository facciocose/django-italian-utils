from django.core.management.base import BaseCommand, CommandError
import zipfile
import re
import csv
from django.utils.six import PY3


class Command(BaseCommand):
    args = '<file_zip>'
    help = "Importa l'elenco dei comuni proveniente dal sito istat"

    def handle(self, *args, **options):
        try:
            zfile = zipfile.ZipFile(args[0])
            found = None

            for filename in zfile.namelist():
                comuni_re = re.compile(r'.+comuni_italiani.+\.csv$')
                if comuni_re.match(filename):
                    found = filename
                    break
            if not found:
                raise CommandError('File dei comuni non trovato')

            csvstring = zfile.read(found)
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
                print(row)
                break

        except IndexError:
            raise CommandError('Nessun file specificato')
        except IOError:
            raise CommandError('File non trovato o corrotto')


        #zipfile.ZipFile()
#        print(options['file_zip'])
#        self.stdout.write('ok')
