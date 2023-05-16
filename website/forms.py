from django.forms import ModelForm
from .models import *

class CreateTeamForm(ModelForm):

    class Meta:
        model = Team
        fields = ["city", "name"]