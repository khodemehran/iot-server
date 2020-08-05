from django.db import models

# Create your models here.
class Data(models.Model):

    humidity = models.FloatField(max_length=3)
    temp = models.FloatField(max_length=3)
    date = models.DateTimeField()
    tozih = models.CharField(max_length=300)



    def __str__(self):
        return self.tozih




