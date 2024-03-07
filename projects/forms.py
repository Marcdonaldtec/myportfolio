from .models import Project
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model =Project
        fields =['user','title','description','technology_used','link','image']
        