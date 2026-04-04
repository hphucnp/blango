
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render

from assessment.models import Thing
from blog.forms import CommentForm
from blog.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def question2(request):
    return render(request, 'question2.html')


def question4(request):
    user_model = get_user_model()
    owner, _ = user_model.objects.get_or_create(
        username='question4-owner',
        defaults={'first_name': 'Question', 'last_name': 'Owner'},
    )
    thing, _ = Thing.objects.get_or_create(name='Question 4 Thing', owner=owner)

    if not thing.comments.exists():
        thing.comments.create(content='Zulu')
        thing.comments.create(content='Alpha')
        thing.comments.create(content='Bravo')

    return render(request, 'question4.html', {'thing': thing})


def post_detail(request, slug):
    # post = get_object_or_404(Post, slug=slug)
    # return render(request, 'blog/post-detail.html', {'post': post})
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, 'blog/post-detail.html', {'post': post, 'comment_form': comment_form})