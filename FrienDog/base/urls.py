from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('profiles/', views.profiles_page, name='profiles'),
    path('profile-form/', views.profile_form, name='profile_form'),
    path('fill-form-prompt/', views.fill_form_prompt, name='fill_form_prompt'),
    path('edit-form/<str:pk>/', views.edit_form, name='edit_form'),
    path('delete-profile/<str:pk>/', views.delete_profile, name='delete_profile'),
]