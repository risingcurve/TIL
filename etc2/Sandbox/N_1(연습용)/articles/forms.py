from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = "Title",
        widget = forms.TextInput(
            attrs={
            #    'class' :  'my-title',
                'placeholder' : '입력해주세요 제목을',
                'maxlength': 10,
            }
        ),
        error_messages = {
            'required': 'give me title!'
        },
    )

    content = forms.CharField(
        label = "Content",
        widget = forms.Textarea(
            attrs={
                # 'class' : 'my-content',
                'placeholder' : '입력해주세요! 콘텐츠를',
                'rows': 4,
            }
        ),
        error_messages = {
            'required': 'give me content!'
        },
    )

    class Meta:
        model = Article
        fields = '__all__'