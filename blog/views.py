from django.shortcuts import get_object_or_404, render

from blog.models import Post


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': post})
