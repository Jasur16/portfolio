from django.db import models

class HomeImageModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='homw_image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'home'