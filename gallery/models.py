from django.db import models
  
# Create your models here.

class Category(models.Model):
    Category_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.Category_name

    def save_category(self):
        self.save()

class Description(models.Model):
    Description_name = models.CharField(max_length = 30)   


    def __str__(self):
        return self.Description_name

    def save_description(self):
        self.save()   


class Location(models.Model):
    Location_name = models.CharField(max_length = 30)


    def __str__(self):
        return self.Location_name

    def save_location(self):
        self.save()   



class Photo(models.Model):
    title = models.CharField(max_length  = 60)
    location_name = models.ForeignKey(Location)
    category_name = models.ForeignKey(Category)
    image = models.ImageField(upload_to = 'photo/')


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    


    @classmethod
    def search_by_location(cls,search_term):
        photo = cls.objects.filter(title_icontains = search_term)
        return photo   


    @classmethod
    def get_image_by_id(cls,Location):
        image = cls.objects.get(id=input_id)
        return image     




