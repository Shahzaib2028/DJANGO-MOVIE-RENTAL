from django import forms
from . import models

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movies
        fields = ['movie_name', 'movie_year', 'movie_genere', 'price']
        widgets = {
            'movie_name': forms.TextInput(attrs={'class':'form-control'}),
            'movie_year': forms.TextInput(attrs={'class':'form-control'}),
            'movie_genere': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Members
        fields = ['member_name', 'member_address']
        widgets = {
            'member_name': forms.TextInput(attrs={'class':'form-control'}),
            'member_address': forms.TextInput(attrs={'class':'form-control'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class MovieRentalForm(forms.ModelForm):

    return_date = forms.DateInput()
    
    class Meta:
        model = models.Movie_Rental
        fields = ['member_id', 'movie_id', 'return_date']
        widgets = {
            'member_id': forms.Select(attrs={'class':'form-control', 'readonly':'readonly'}),
            'movie_id': forms.Select(attrs={'class':'form-control', 'readonly':'readonly'}),
            'return_date': DateInput(),
        }

    

