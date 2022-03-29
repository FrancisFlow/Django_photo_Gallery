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
 
 class ImageTestClass(TestCase):

     def setUp(self):
         self.anime=Category(name='Anime')
         self.anime.save_category()

         self.location=Location(name='Sweden')
         self.location.save_location()

         self.new_image=Image(image_name='Kaizen', image_description='The supreme masters of ninja', image_category=selr.anime, image_location=self.location)
         self.new_image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
    
    
    def test_get_images(self):
        all_images = Image.get_images()
        self.assertTrue(len(all_images)>0)
     
    def test_filter_by_location(self):
        test_location_id = 6
        images_location = Image.filter_by_location(test_location_id) 
        self.assertTrue(len(images_location) == 0)  

    