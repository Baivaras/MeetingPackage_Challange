from django.test import TestCase, Client


class TestVenues(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_nearby_venues_with_no_params(self):
        response = self.client.get('/api/venues/get-nearby-venues/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Missing parameters latitude, longitude or radius')

    def test_get_nearby_venues_with_params(self):
        response = self.client.get('/api/venues/get-nearby-venues/?lat=60.1814921&lon=24.8840972&radius=100')
        self.assertEqual(response.status_code, 200)

    def test_get_nearby_venues_with_invalid_params(self):
        response = self.client.get('/api/venues/get-nearby-venues/?lat=60.1814921&lon=24.8840972&radius=')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Missing parameters latitude, longitude or radius')

    def test_get_nearby_venues_with_invalid_params_2(self):
        response = self.client.get('/api/venues/get-nearby-venues/?lat=60.1814921&lon=&radius=100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Missing parameters latitude, longitude or radius')

    def test_get_nearby_venues_with_invalid_params_3(self):
        response = self.client.get('/api/venues/get-nearby-venues/?lat=&lon=24.8840972&radius=100')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Missing parameters latitude, longitude or radius')
