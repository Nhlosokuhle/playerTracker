from django.forms import ModelForm
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'skill_level', 'eligible_for_selection']
