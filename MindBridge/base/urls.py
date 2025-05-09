<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discussion/<str:pk>/', views.discussion, name='discussion'),
    path('create-discussion/', views.create_discussion, name='create-discussion'),
    path('update-discussion/<str:pk>/', views.update_discussion, name='update-discussion'),
    path('delete-discussion/<str:pk>/', views.delete_discussion, name='delete-discussion'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('sign-up/', views.signup_page, name='sign-up'),
    path('', views.home, name='home'),
    path('discussion/<str:pk>/', views.discussion, name='discussion'),
    path('user-profile/<str:pk>/', views.user_profile, name='user-profile'),
    path('create-discussion/', views.create_discussion, name='create-discussion'),
    path('update-discussion/<str:pk>/', views.update_discussion, name='update-discussion'),
    path('delete-discussion/<str:pk>/', views.delete_discussion, name='delete-discussion'),
    path('delete-answer/<str:pk>/', views.delete_answer, name='delete-answer'),
]
>>>>>>> master
