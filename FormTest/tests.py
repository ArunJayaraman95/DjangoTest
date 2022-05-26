from django.test import TestCase
from .forms import CartoonForm

# Create your tests here.
class TestForms(TestCase):
    
    def test_valid(self):
        form = CartoonForm(data = {
            "cartoon_name": "Hello",
            "episode_count": 45,
            "date_finished": "2000-01-01T12:00",
            "rating": 1.2
        })

        self.assertTrue(form.is_valid())

    def test_episode_missing(self):
        form = CartoonForm(data = {
            "cartoon_name": "Hello",
            "date_finished": "2000-01-01T12:00",
            "rating": 1.2
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_cartoon_no_data(self):
        form = CartoonForm(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)