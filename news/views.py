from django.shortcuts import render, redirect
from .models import Post, Application
from django.http import FileResponse

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'news/post_list.html', {'posts' : posts})

def application_list(request):
    if request.user.is_superuser:
        applications = Application.objects.all().order_by('published_date')
        return render(request, 'applications/application_list.html', {'applications' : applications})
    return redirect('post_list')

def application_download_last(request):
    application = Application.objects.all().order_by('published_date')[:1].get()
    return render(request, 'applications/application_last.html', {'application' : application})