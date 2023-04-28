from django.shortcuts import render,redirect

# Create your views here.
from .models import Post
from .forms import CommentForm

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog/homepage.html', {'posts': posts})


def deatail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

        return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html', {'post': post, 'form': form})


