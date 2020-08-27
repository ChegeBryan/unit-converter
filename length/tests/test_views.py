from django.test import TestCase, Client
from django.urls import reverse


class TestLengthConversion(TestCase):
    """
    This class contains tests that convert measurements from one unit
    of measurement to another
    """

    def setUp(self):
        """
        This method runs before the execution of each test case
        """
        self.client = Client()
        self.url = reverse('length:convert')

    def test_view_exists_at_desired_url(self):
        response = self.client.get('/length/convert/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_centimetre_to_metre_conversion(self):
        """
        Test conversion of centimetre measurements to metre.
        """

        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": round(1234.987, 3)

        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 12.350)

    def test_centimetre_to_mile_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "mile",
            "input_value": round(985805791.3527409, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 6125.511)
