from django.db import models

# Create your models here.

class Overtreding(models.Model):
    
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.CharField(max_length = 500)
    street = models.CharField(max_length = 500)
    driving_direction = models.CharField(max_length = 500)
    speed_limit = models.IntegerField()
    passersby = models.IntegerField()
    infractions_speed = models.IntegerField()
    infractions_red_light =  models.IntegerField()
    
    def __str__(self):
        return self.infractions_speed


