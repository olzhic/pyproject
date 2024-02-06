from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from .models import Like
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(self.request, 'blog.html', {'post_list':posts})


method_decorator(login_required, "get")
class PostDetail(View):
    def get(self, request, pk):
        
        post = Post.objects.get(id = pk)
        return render(request, 'blog_detail.html', {'post':post})

method_decorator(login_required, "post")
class AddComments(View):
    
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')
    
    