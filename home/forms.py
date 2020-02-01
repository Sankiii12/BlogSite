#from django import forms

#class contactform(forms.Form):
#    name=forms.CharField(max_length=50)
#    email=forms.EmailField(max_length=50)
#    message=forms.CharField(
#        max_length=100000,
#        widget=forms.Textarea(),
#        help_text='Write Your message here'
#        )

from django.forms import ModelForm
from home.models import contactus
class contactform(ModelForm):
    class Meta:
        model=contactus
        fields=['name','email','message']
