from django import forms
from .models import Post
class BlogForm(forms.ModelForm):
    #caption = forms.CharField(required=False, Widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['name','caption','image','author','profile']
        widgets = {
            'caption': forms.Textarea(attrs={'cols': 20, 'rows': 10}),
        }