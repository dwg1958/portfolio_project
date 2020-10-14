##########################################
# PICTURES APP DATA MODELS ###############
##########################################
from django.db import models

# Create your models here.
class Picture(models.Model):
    image       = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)

    #Change picture title in admin panel
    def __str__(self):
        return self.description
