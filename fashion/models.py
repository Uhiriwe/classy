from django.db import models

# Create your models here.
class classy(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to='image/')
    discription = models.TextField()

    def __str__(self):
        return self.title

