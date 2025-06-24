from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    PostForm is a Django ModelForm for creating and editing Post objects.
    This form automatically generates fields for the 'title' and 'text' attributes of the Post model.
    It is used to collect user input for new blog posts or to update existing ones.
    Usage:
        - Use this form in your views to handle blog post creation and editing.
        - The form will display input fields for 'title' and 'text'.
        - On submission, validated data can be saved directly to the database as a Post instance.
    Attributes:
        Meta:
            model (Post): The model that this form is linked to.
            fields (list): The fields from the Post model to include in the form ('title' and 'text').
    """
    
    class Meta:
        model = Post
        fields = ['title', 'text']