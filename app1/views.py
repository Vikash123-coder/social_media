

from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from .forms import signUpForm
from .models import Profile
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView


# Create your views here.
def deshboard(request):
    if request.user.is_authenticated:
        return render(request, 'deshboard.html')
    else:
       return HttpResponseRedirect('/login/')  
def sign_up(request):
    if request.method=='POST':
       fm = signUpForm(request.POST) 
       if fm.is_valid():
          messages.success(request, 'submit success!')
          fm.save()
          return HttpResponseRedirect('/login/')
    else:        
        fm = signUpForm()
    return render(request, 'sign_up.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                   login(request, user)
                   messages.success(request, 'login success!')
                return HttpResponseRedirect('/')
        else:            
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/')
def user_logout(request):
    
    logout(request)
    return HttpResponseRedirect('/login/')

def follow_unfollow_profile(request):
    if request.method=="POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)
        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profile-list-view')            
        

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profiles' # object_list as default
    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)    
       my_profile = Profile.objects.get(user=self.request.user)
       posts = Post.objects.filter(author=self.request.user)
       context['image'] = my_profile.image
       context['name'] = my_profile
       context['posts'] = posts
       return context
       

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/detail.html'
    
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        #print(view_profile)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        
        if view_profile.user in my_profile.following.all():
            follow = True
            
        else:
            follow = False
        #context["image"] = view_profile.image     
        context["follow"] = follow
        return context 



