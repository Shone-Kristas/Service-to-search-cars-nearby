from django.core.management.base import BaseCommand
from myapp.urls import load_data_from_csv

class Command(BaseCommand):
    help = 'Load data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        load_data_from_csv(file_path)
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))