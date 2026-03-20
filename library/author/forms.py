from django import forms

from .models import Author

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic',)

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter surname'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patronymic'}),
        }