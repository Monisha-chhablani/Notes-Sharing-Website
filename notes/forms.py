from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'desc']
        labels = {'title': 'Title', 'desc': 'Description'}
        widgets = {'title': forms.TextInput(
            attrs={'class': 'form-control'}), 'desc': forms.Textarea(attrs={'class': 'form-control'}), }
# class CommentForm(forms.ModelForm):
#     class Meta():
#         model = Comment
#         fields =  ('author','title')
#         widgets = {
#             'author':forms.TextInput(attrs={'class':'textinputclass'}),
#             'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea '})
#             }


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

