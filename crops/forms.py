from django import forms
from .import models

class AddCrop(forms.ModelForm):
    class Meta:
        model = models.Crop
        fields = ['name',
                'start_date',
                'est_harvest',
                'problem',
                'image']

class AddQuery(forms.ModelForm):
    class Meta:
        model = models.Query
        fields = ['problem_desc','reported_date','image']