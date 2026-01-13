import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Satellite(models.Model):
    def __str__(self):
        return self.satellite_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    satellite_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Pick(models.Model):
    def __str__(self):
        return self.pick_text

    satellite = models.ForeignKey(Satellite, on_delete=models.CASCADE)
    pick_text = models.CharField(max_length=200)
    vehicle = models.IntegerField(default=0)