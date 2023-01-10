from django.urls import path
from .views import ProfileListView, ProfileDetailView,follow_unfollow_profile
app_name = 'app1'

urlpatterns = [
    path('',ProfileListView.as_view(), name = 'profile-list-view'),
    path('switch_follow/', follow_unfollow_profile, name='follow_unfollow_view'),
    path('<pk>/',ProfileDetailView.as_view(), name = 'profile-detail-view'),
]