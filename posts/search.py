from re import search
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request):
    
    return render(request, 'profiles/deshboard.html')

def get_names(request):
    search = request.GET.get('search')
    payload=[]
    if search:
        objs = User.objects.filter(username__startswith=search)
        for obj in objs:
            payload.append({
                'username':obj.username
            })
    
    return JsonResponse({
       'status':True,
       'payload':payload
    })    
