# Import the necessary Django modules
from django.db import models  # lets us define models (i.e., database tables)
from django.conf import settings  # gives access to project settings (like the user model)
from django.utils import timezone  # helps us deal with date and time

# Define a model (i.e., table) named 'Post'
class Post(models.Model):
    # This links each post to a user (the author).
    # settings.AUTH_USER_MODEL means it uses the built-in User model.
    # on_delete=models.CASCADE means: if the user is deleted, delete their posts too.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # A short text field for the title of the post, max 200 characters
    title = models.CharField(max_length=200)
    
    # A large text field for the body/content of the post
    text = models.TextField()
    
    # Automatically set the date/time when a post is created
    created_date = models.DateTimeField(default=timezone.now)
    
    # Date/time when the post is published — optional (can be blank or null)
    published_date = models.DateTimeField(blank=True, null=True)
    
    # Method to publish the post by setting the published_date to now and saving it
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    # This defines how the post will look when printed or shown in the admin panel
    def __str__(self):
        return self.title
