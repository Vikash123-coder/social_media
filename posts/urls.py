from django.urls import path
from .views import ShowBlog
from .search import get_names, index
app_name = 'posts'

urlpatterns = [
      path('', index),
      path('add/', ShowBlog, name='post'),
      path('get-names/', get_names, name='get-names')
]