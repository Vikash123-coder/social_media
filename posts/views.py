from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from .forms import BlogForm
# Create your views here.


def ShowBlog(request):
    if request.method=="POST":
        fm = BlogForm(request.POST,request.FILES)
        # name = fm.cleaned_data['name']
        # caption = fm.cleaned_data['caption']
        # image = fm.cleaned_data['image']
        if fm.is_valid():
            #id = User.objects.get(user=request.user)
            current_post=fm.save(commit=True)
            current_post.save()
            return HttpResponseRedirect('/profiles/')
    else:        
        fm = BlogForm()
        return render(request, 'posts/post.html',{'form':fm})