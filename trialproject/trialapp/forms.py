from django.forms import ModelForm
from .models import projects

class ProjectForm(ModelForm):
    class Meta:
        model=projects
        fields=['Title','description','feature_image','demo_link','source_link','tags']