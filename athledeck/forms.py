from django import forms

from .models import Athlete

class AthleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AthleteForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
          field = self.fields.get(field_name) 
          field.widget = forms.TextInput(attrs={'placeholder': field.label, 'class': 'form-control', 'label': ''})

    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'sport', 'league', 'team', 'bio')