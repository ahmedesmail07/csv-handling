from django.db import models

class Restaurants(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=30)
    items = models.TextField()
    lat_long = models.TextField(max_length=45)
    full_details = models.TextField()
   