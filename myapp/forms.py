from django import forms
from myapp.models import UserModel, PostModel, LikeModel, CommentModel


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'name', 'password']


    #forms.py
class LoginForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image', 'caption']


class LikeForm(forms.ModelForm):
    class Meta:
        model = LikeModel
        fields=['post']


class CommentForm(forms.ModelForm):
  class Meta:
    model = CommentModel
    fields = ['comment_text', 'post']