from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

    

class Photo(models.Model):
    file1 = models.ImageField()
    file12 = models.ImageField()
    file3 = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'