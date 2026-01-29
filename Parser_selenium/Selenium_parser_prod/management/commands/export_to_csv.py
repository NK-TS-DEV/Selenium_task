from django.core.management.base import BaseCommand
from Selenium_parser_prod.services.exportFile_to_csv import export_products_to_csv


class Command(BaseCommand):
    help = 'Export products from database to CSV file'

    def handle(self,*args, **options):
        self.stdout.write( "Starting export...")

        export_products_to_csv()

        self.stdout.write(self.style.SUCCESS( "Success! File 'brain_products.csv' created."))