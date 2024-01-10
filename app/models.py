from django.db import models

#Create your models here.
class Conect(models.Model):
    company = models.CharField(null=False, blank=False)
    text = models.CharField(max_length=2000, null=False, blank=False)
    image = models.ImageField(upload_to="image")
    description_image = models.CharField(max_length=2000)
    spreadsheet = models.FileField(upload_to="xlsx")
    date_added = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    
    def __str__(self) -> str:
        return self.company