from django.db import models  
  
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

class Location(models.Model):
    location_name = models.CharField(max_length = 30)


    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()   



class Photo(models.Model):
    title = models.CharField(max_length  = 60)
    location_name = models.ForeignKey(Location)
    category_name = models.ForeignKey(Category)
    photo = models.ImageField(upload_to = 'photo/')


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    


    @classmethod   
    def search_by_location(cls,search_term):
        photo = cls.objects.filter(location_name__location_name__icontains = search_term)
        return photo  


    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category_name__category_name__icontains = search_term)
        return photo  


    @classmethod
    def get_photo_by_id(cls,Location):
        photo = cls.objects.get(id=input_id)
        return photo     




