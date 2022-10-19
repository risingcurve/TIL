from django import forms
from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = '__all__'


class CommentForm(forms.ModelForm):
    PICK_A = False
    PICK_B = True
    PICKS = [
        (PICK_A, 'BLUE'),
        (PICK_B, 'RED'),
    ]

    pick = forms.ChoiceField(choices=PICKS)

    # radio
    # pick = forms.ChoiceField(choices=PICKS, widget=forms.RadioSelect)


    class Meta:
        model = Comment
        # 1. exclude (tuple)
        # 2. fields
        fields = ['pick', 'content'] # 문자


