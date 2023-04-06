from django.db import models

# Create your models here.
class Player(models.Model):
    """
    A model representing a player in a sports team.

    Inherits from Django's Model class and defines the fields of the player object.

    :param models.Model: A built-in Django class that represents a database table and its associated fields.
    :type models.Model: class
    """
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    skill_level = models.IntegerField(default=0)
    eligible_for_selection = models.BooleanField() 

def __str__(self):
    """
    Returns a string representation of the player object.

    :return: A string representation of the player object, consisting of the player's first name.
    :rtype: str
    """
    return self.first_name