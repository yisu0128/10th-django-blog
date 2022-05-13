from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from django.utils import timezone
from .forms import BlogForm

# Create your views here.


def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def new(request):
    form = BlogForm
    return render(request, 'new.html', {'form': form})


def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid:
        new_blog = form.save(commit=False)
        new_blog.date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('detail', blog_id=blog.pk)
        else:
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'edit.html', {'form': form})


def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')
