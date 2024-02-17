import csv
from django.core.management.base import BaseCommand
from patients.models import Patient
from orders.models import Order
from results.models import Result


class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:

                patient, created = Patient.objects.get_or_create(
                    id=row['patientId'],
                    name=row['patientName'],
                    surname=row['patientSurname'],
                    sex=row['patientSex'],
                    birth_date=row['patientBirthDate']
                )

                order, created = Order.objects.get_or_create(
                    patient=patient,
                    id=row['orderId']
                )

                Result.objects.create(
                    order=order,
                    name=row['testName'],
                    value=row['testValue'],
                    reference=row['testReference']
                )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
