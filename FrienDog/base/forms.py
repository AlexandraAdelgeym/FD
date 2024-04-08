from django.forms import ModelForm
from .models import Profile

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
