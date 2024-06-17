from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    name = models.CharField(max_length=100)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0)  

    class Meta:
        unique_together = ('user', 'area')  
