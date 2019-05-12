from django.test import TestCase
from .models import Category,Photo,Location


# Create your tests here.
class photo_TestCases(TestCase):
    def setUp(self):
        self.new_location = Location(location_name = 'Oslo')
        self.new_location.save_location()
        self.new_category = Category(category_name = 'Fashion')
        self.new_category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_photo,Photo))
        self.assertTrue(isinstance(self.new_location,Location))
        self.assertTrue(isinstance(self.new_category,Category))

    def test_search_by_category(self):
        self.new_image.save_image()
        instance = Category.objects.get(category_name='Fashion')
        self.assertTrue(instance.category_name=='Fashion')



    def test_search_by_location(self):
        self.new_image.save_image()
        instance = Location.objects.get(location_name='Oslo')
        self.assertTrue(instance.location_name=='Oslo')
    

