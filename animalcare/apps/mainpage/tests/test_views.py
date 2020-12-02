
from django.test import TestCase
 
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """La página raíz se carga correctamente"""
        response = self.client.get('http://localhost:8000/index')
        self.assertEqual(response.status_code, 200)

    def test_donaciones_loads_properly(self):
        """La página donaciones se carga correctamente"""
        response = self.client.get('http://localhost:8000/donaciones')
        self.assertEqual(response.status_code, 200)
    

    def test_afrikc_loads_properly(self):
        """La página raíz se carga correctamente"""
        response = self.client.get('http://localhost:8000/africa')
        self.assertEqual(response.status_code, 200)

    def test_oceania_loads_properly(self):
        """La página oceania se carga correctamente"""
        response = self.client.get('http://localhost:8000/oceania')
        self.assertEqual(response.status_code, 200)
    
    def test_asia_loads_properly(self):
        """La página asia se carga correctamente"""
        response = self.client.get('http://localhost:8000/asia')
        self.assertEqual(response.status_code, 200)
    
    def test_europa_loads_properly(self):
        """La página europa se carga correctamente"""
        response = self.client.get('http://localhost:8000/europa')
        self.assertEqual(response.status_code, 200)

    def test_america_loads_properly(self):
        """La página america se carga correctamente"""
        response = self.client.get('http://localhost:8000/europa')
        self.assertEqual(response.status_code, 200)