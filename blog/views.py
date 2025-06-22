# This file is used to handle what happens when someone visits a page on your website.

# Import the render function, which helps us show an HTML page to the user
from django.shortcuts import render

# This is where we define our views (what the user sees)

# Create your views here.
# This is a function called post_list. It will be used when someone visits the homepage or a blog list page.
def post_list(request):
    # 'request' is the information coming from the user (like which page they want to visit)

    # This function uses the render() method to show an HTML page
    # - 'request' is the user's request
    # - 'blog/post_list.html' is the path to the HTML file we want to show
    # - {} is a dictionary where we can add data we want to display in the template (empty for now)
    return render(request, 'blog/post_list.html', {})
