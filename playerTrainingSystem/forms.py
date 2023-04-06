from django.forms import ModelForm
from .models import Player

"""
    A form used for creating and updating player objects.

    Inherits from Django's ModelForm class and uses the Player model to define the form fields.

    :param ModelForm: A built-in Django form class that creates a form based on a specified model.
    :type ModelForm: class
    """

class PlayerForm(ModelForm):
    """
        Metadata for the PlayerForm class.

        Specifies that the form should be based on the Player model and should include only the first_name, last_name,
        skill_level, and eligible_for_selection fields.

        :param model: The model that the form should be based on.
        :type model: Model
        :param fields: The fields that should be included in the form.
        :type fields: list
        """
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'skill_level', 'eligible_for_selection']
