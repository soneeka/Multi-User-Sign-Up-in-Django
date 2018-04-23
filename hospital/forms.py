from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    post=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'write post here...'}))
    Medicines=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Medicines'}))
    Documents=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Attach documents'}))
    
    
    class Meta:
        model = Post
        fields=('Medicines','post','Documents')