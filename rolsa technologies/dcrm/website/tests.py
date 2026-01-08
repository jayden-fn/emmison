from django.test import TestCase
from django.urls import reverse

class CalculateViewTests(TestCase):
    def test_calculate_post(self):
        url = reverse('calculate')
        data = {
            'distance': '100',
            'consumption': '6',  # L per 100 km
            'price': '1.50',
            'emission_factor': '2.31'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        # fuel used = 100 * 6 / 100 = 6 L
        # cost = 6 * 1.5 = 9.0
        # emissions = 6 * 2.31 = 13.86
        self.assertContains(response, 'Fuel used: 6.0')
        self.assertContains(response, 'Cost: 9.00')
        self.assertContains(response, 'Estimated emissions: 13.86')


class BookingViewTests(TestCase):
    def test_booking_get(self):
        url = reverse('booking')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Request a Booking')

    def test_booking_post_success(self):
        url = reverse('booking')
        data = {
            'name': 'Alice',
            'email': 'alice@example.com',
            'phone': '0123456789',
            'service': 'Solar install',
            'date': '2025-12-20',
            'message': 'Please call to confirm.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking Submitted')
        self.assertContains(response, 'Alice')
        self.assertContains(response, 'alice@example.com')
