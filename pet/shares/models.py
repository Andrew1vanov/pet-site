from django.db import models
from django.urls import reverse

# Create your models here.

class Security(models.Model):
    sec_name = models.CharField(max_length = 300)
    sec_short_name = models.CharField(max_length = 100)
    sec_id = models.CharField(max_length = 10)
    border = models.CharField(max_length = 4)

    def __str__(self):
        return self.sec_name

    def get_absolute_url(self):
        return reverse('security_detail', args=[str(self.id)])