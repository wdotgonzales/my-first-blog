from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    """
    Handles HTTP request to display a list of blog posts.

    This view function retrieves all Post objects from the database that have a published_date
    less than or equal to the current time (i.e., posts that have already been published).
    The posts are ordered by their published_date in ascending order (oldest first).
    It then renders the 'blog/post_list.html' template, passing the list of posts to the template
    so they can be displayed on the web page.

    Args:
        request: The HTTP request object sent by the user's browser.

    Returns:
        HttpResponse: The rendered HTML page showing the list of published blog posts.
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    View function to display the details of a single blog post.

    Args:
        request: The HTTP request object sent by the user's browser.
        pk (int): The primary key (unique ID) of the blog post to display.

    Returns:
        HttpResponse: Renders the 'blog/post_detail.html' template with the post data.

    For Dummies:
        - This function is called when someone wants to see a specific blog post.
        - It looks for a post with the given 'pk' (post ID). If it doesn't exist, it shows a 404 error (page not found).
        - If the post exists, it shows the post details using a web page template.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    """
    Handles the creation of a new blog post.

    If the request method is POST, this view processes the submitted form data to create a new blog post.
    - It checks if the form is valid.
    - If valid, it creates a new post object, assigns the current user as the author, sets the published date to now, and saves the post.
    - After saving, it redirects the user to the detail page of the newly created post.

    If the request method is not POST (usually GET), it displays an empty form for the user to fill out.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: Renders the post edit form template if GET, or redirects to the post detail page if POST and form is valid.

    Note:
        - This view requires the user to be authenticated.
        - The form used is PostForm, which should be defined elsewhere in your code.
        - The template rendered is 'blog/post_edit.html'.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    """
    Edit an existing blog post.

    This view handles both displaying the edit form for a blog post and processing the form submission.
    - If the request method is GET, it shows a form pre-filled with the post's current data.
    - If the request method is POST, it updates the post with the submitted data if the form is valid.

    Args:
        request (HttpRequest): The HTTP request object. Can be GET (to show the form) or POST (to submit changes).
        pk (int): The primary key (ID) of the post to edit.

    Returns:
        HttpResponse: 
            - If GET: Renders the 'post_edit.html' template with the form.
            - If POST and form is valid: Redirects to the post's detail page.
            - If POST and form is invalid: Renders the form again with error messages.

    Note:
        - Only logged-in users should be able to edit posts (make sure to add authentication checks if needed).
        - The form used is 'PostForm', and the template is 'blog/post_edit.html'.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})