from django import forms
from base.models import *

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'description': forms.Textarea(attrs={"rows": "5", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
 }
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('__all__')
        widgets = {
            'sector': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'overview': forms.Textarea(attrs={"rows": "5", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'article': forms.Textarea(attrs={"rows": "10", 'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ('__all__')
        widgets = {
            'sector': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'title': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'subtitle': forms.TextInput(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'article': forms.Textarea(attrs={"rows": "10",'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
            'role': forms.Select(attrs={'class': "mb-2 px-4 py-2 rounded-md bg-white w-full"}),
        }
