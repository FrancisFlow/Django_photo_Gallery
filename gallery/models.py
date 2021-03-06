from django.db import models

# Create your models here.

class Image(models.Model):
    image=models.ImageField(upload_to='images/', blank=True)
    image_name=models.CharField(max_length=200)
    image_description=models.TextField()
    image_location=models.ForeignKey('Location', on_delete=models.CASCADE)
    image_category=models.ForeignKey('Category', on_delete=models.CASCADE)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def get_images(cls):
        all_images=cls.objects.all()
        return all_images
    
    @classmethod
    def search_by_category(cls, search_term):
        images= cls.objects.filter(image_category__name__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls, id):
        images_by_location=cls.objects.filter(image_location=id)
        return images_by_location
class Location(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    def get_locations(cls):
        locations=cls.objects.all()
        return locations

class Category (models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()