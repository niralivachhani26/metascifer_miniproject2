from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('story/', views.story, name='story'),
    path('story_details/', views.story_details, name='story_details'),
    path('members/', views.members, name='members'),
    path('contact/', views.contact, name='contact'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('send_friend_request/<int:receiver_id>', views.send_friend_request, name='send_friend_request'),
    path('respond_friend_request/<int:request_id>/<str:action>/', views.respond_to_friend_request, name='respond_to_friend_request'),

]