from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.sweden=Location(name='Sweden')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.sweden, 'Sweden'))
    def test_save_method(self):
        self.sweden.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    

class CategoryTestClass(TestCase):
    def setUp(self):
        self.anime=Category(name='Anime')
    def test_instance(self):
        self.assertTrue(isinstance(self.anime.name, 'Anime'))
    def test_save_method(self):
        self.anime.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    