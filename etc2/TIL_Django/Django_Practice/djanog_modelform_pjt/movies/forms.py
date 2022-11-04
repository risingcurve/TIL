from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    comedy = 'comedy'
    horror = 'horror'
    romance = 'romance'

    GENRE_CHOICE = [
        (comedy, '코미디'),
        (horror, '공포'),
        (romance, '로맨스'),
    ]

    genre = forms.ChoiceField(
        label = 'Genre',
        choices = GENRE_CHOICE,
        widget = forms.Select()
    )

    release_date = forms.DateField(
        widget = forms.DateInput(
            attrs = {
                'type': 'date',
            }
        )
    )

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': 0.5,
                'min': 0,
                'max': 5,
                'placeholder': 'Score',
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
