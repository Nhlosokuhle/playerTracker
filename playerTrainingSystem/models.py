from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    skill_level = models.IntegerField(default=0)
    eligible_for_selection = models.BooleanField() 

def __str__(self):
    return self.first_name