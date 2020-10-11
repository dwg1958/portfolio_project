from django.db import models

# Create your models here.
class Blog(models.Model):
    title     = models.CharField(max_length=100)
    date      = models.DateTimeField(auto_now=False, auto_now_add=False)
    image     = models.ImageField(upload_to='blogImages/')
    bodycopy  = models.TextField()

    #Summary text block
    def summary(self):
        return self.bodycopy[:1000]

    # Date presentation - - see https://strftime.org/
    def pub_date_pretty(self):
        return self.date.strftime('%A %b %e, %Y')

    #Change post title in admin panel
    def __str__(self):
        return(self.date.strftime('%x') + " - " + self.title)
