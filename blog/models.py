from django.db import models

# Create your models here.
class Blog(models.Model):
    title     = models.CharField(max_length=100)
    date      = models.DateTimeField(auto_now=False, auto_now_add=False)
    image     = models.ImageField(upload_to='blogImages/')
    bodycopy  = models.TextField()
