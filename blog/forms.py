
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from bs4 import BeautifulSoup  # Install BeautifulSoup if not already installed


choice_list = []
choices = Category.objects.all().values_list('name', 'name')
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = Category.objects.all().values_list('name', 'name')
        choice_list = []

        for item in choices:
            choice_list.append(item)
        self.fields['category'].choices = choice_list
        self.fields['body_content'].label = "Question"

    class Meta:
        model = Post
        fields = ( 
                  'author', 'category', 'body_content')
        widgets = {



            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),

            'category': forms.Select(choices=choice_list, attrs={'class': 'form-select '}),

            'body_content': SummernoteWidget(   attrs={
                

                'summernote': {
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['fontsize', ['fontsize']],
                        ['color', ['forecolor', 'backcolor']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['insert', ['link', 'picture', 'video', 'table', 'hr']],
                        ['misc', ['codeview']],
                        # Add or remove menu items as needed
                    ],
                     'disableResizeEditor': False,
                    'placeholder': 'Ask Your Question Anonymous 👩‍🚀👩‍🚀',
                }
            }),
        }

    def clean_content(self):
        content = self.cleaned_data.get('body_content', '')
        # Extract text content from HTML using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        text_content = soup.get_text()
        return text_content

class PostFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = Category.objects.all().values_list('name', 'name')
        choice_list = []

        for item in choices:
            choice_list.append(item)
        self.fields['category'].choices = choice_list
        self.fields['body_content'].label = "Question"

    class Meta:
        model = Post
        fields = ( 
                 'category', 'body_content')
        widgets = {




            'category': forms.Select(choices=choice_list, attrs={'class': 'form-select '}),

            'body_content': SummernoteWidget(   attrs={
                

                'summernote': {
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['fontsize', ['fontsize']],
                        ['color', ['forecolor', 'backcolor']],
                        ['para', ['ul', 'ol', 'paragraph']],
                        ['insert', ['link', 'picture', 'video', 'table', 'hr']],
                        ['misc', ['codeview']],
                        # Add or remove menu items as needed
                    ],
                     'disableResizeEditor': False,
                    'placeholder': 'Ask Your Question Anonymous 👩‍🚀👩‍🚀',
                }
            }),
        }


