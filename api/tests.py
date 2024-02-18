from django.core.management import call_command
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.test import APIClient
from rest_framework import status

from patients.models import Patient
from orders.models import Order
from results.models import Result


class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.refresh_token = str(RefreshToken.for_user(self.user))

    def test_login(self):
        url = reverse('login')
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_login_user_not_found(self):
        url = reverse('login')
        data = {'username': 'non_existent_user', 'password': self.password}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_wrong_password(self):
        url = reverse('login')
        data = {'username': self.username, 'password': 'wrong_password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh(self):
        url = reverse('refresh')
        data = {'refresh': self.refresh_token}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


class APITest(TestCase):
    @classmethod
    def setUpClass(cls):  # Calling mgmt command from setUpClass prevents it from running for each test
        super().setUpClass()
        call_command('load_data_from_csv', 'data_management/data/results.csv')

    def setUp(self):
        self.client = APIClient()
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_user_exists(self):
        test_id = 1
        url = reverse('patient-profile', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_structure = {'patient': {'id': 1, 'name': 'Piotr', 'surname': 'Kowalski', 'sex': 'm', 'birthDate': '1983-04-12'}, 'orders': [{'orderId': 1, 'results': [{'name': 'Protoporfiryna cynkowa', 'value': '4.0', 'reference': '< 40,0'}, {'name': 'Wolna trijodotyronina (FT3) (O55)', 'value': '4.00', 'reference': '2,30 - 4,20'}]}, {'orderId': 2, 'results': [{'name': 'Tyreotropina (TSH)  trzeciej generacji (L69)', 'value': '334,000 µIU/ml', 'reference': '0,550 - 4,780'}, {'name': 'Urobilinogen', 'value': 'prawidłowy', 'reference': 'prawidłowy'}]}]}
        self.assertEqual(response.data, expected_structure)

    def test_user_does_not_exist(self):
        test_id = 999
        url = reverse('result-details', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patients(self):
        patients_array_length = 4
        url = reverse('patients')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), patients_array_length)

    def test_patient_details(self):
        test_id = 2
        url = reverse('patient-details', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_structure = {"id": 2, "name": "Anna", "surname": "Jabłońska", "sex": "female", "birthDate": "2002-12-12"}
        self.assertEqual(response.data, expected_structure)

    def test_patient_update(self):
        test_id = 4
        updated_data = {
            "surname": "Wiśniewska-Bąk",
        }
        url = reverse('patient-update', kwargs={'pk': test_id})
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_instance = Patient.objects.get(pk=test_id)
        self.assertEqual(updated_instance.surname, updated_data["surname"])

    def test_patient_delete(self):
        test_id = 2
        url = reverse('patient-delete', kwargs={'pk': test_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Patient.DoesNotExist):
            deleted_instance = Patient.objects.get(pk=test_id)

    def test_orders(self):
        orders_array_length = 6
        url = reverse('orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), orders_array_length)

    def test_order_details(self):
        test_id = 2
        url = reverse('order-details', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_structure = {"orderId": 2, "patientId": 1, "resultIds": [3, 7]}
        self.assertEqual(response.data, expected_structure)

    def test_order_does_not_exist(self):
        test_id = 999
        url = reverse('order-details', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_order_delete(self):
        test_id = 2
        url = reverse('order-delete', kwargs={'pk': test_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Order.DoesNotExist):
            deleted_instance = Order.objects.get(pk=test_id)

    def test_results(self):
        results_array_length = 9
        url = reverse('results')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), results_array_length)

    def test_result_details(self):
        test_id = 2
        url = reverse('result-details', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_structure = {"id": 2, "name": "Wolna trijodotyronina (FT3) (O55)", "value": "4.00", "reference": "2,30 - 4,20"}
        self.assertEqual(response.data, expected_structure)

    def test_result_does_not_exist(self):
        test_id = 999
        url = reverse('result-details', kwargs={'pk': test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_result_update(self):
        test_id = 4
        updated_data = {
            "value": "60",
        }
        url = reverse('result-update', kwargs={'pk': test_id})
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_instance = Result.objects.get(pk=test_id)
        self.assertEqual(updated_instance.value, updated_data["value"])

    def test_result_delete(self):
        test_id = 2
        url = reverse('result-delete', kwargs={'pk': test_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Result.DoesNotExist):
            deleted_instance = Result.objects.get(pk=test_id)
