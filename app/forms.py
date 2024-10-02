from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    author_full_name = forms.CharField(max_length=200, required=False)
    #existing_author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    author_age = forms.IntegerField(required=False)
    author_languages = forms.CharField(max_length=200, required=False)
    
    class Meta:
        model = Book
        fields = ['title', 'author_full_name', 'author_languages', 'author_age', 'description', 'pages', 'genre']
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Book Title'}),
            'author_full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Author Full Name'}),
            'author_age': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Add Author Age'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Add Book Description'}),
            'genre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Book Genre'}),
            'pages': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Add Number of Pages'}),
            'author_languages': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Author Languages'})
        }
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'age', 'languages']
        
        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Author Full Name'}),
            'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Add Author Age'}),
            'languages': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Add Author Languages'}),
        }
        