from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_blog_loads_properly(self):
        """La página blog se carga correctamente"""
        response = self.client.get('http://localhost:8000/blog/')
        self.assertEqual(response.status_code, 200)

    def test_new_post_loads_properly(self):
        """La página crear post se carga correctamente"""
        response = self.client.get('http://localhost:8000/blog/post/new/')
        self.assertEqual(response.status_code, 200)


    