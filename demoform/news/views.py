from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.

def index(request):
    return HttpResponse("Hello everyone!")

def add_post(request):
    f = PostForm()
    return render(request, 'news/add_post.html', { "f": f })

def save_post(request):
    if request.method == "POST":
        data = PostForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Save successfully')
        else:
            return HttpResponse('Invalid form')
    else:
        return HttpResponse('Invalid post request')