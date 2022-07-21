from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signIn, name="signin"),
    path('signout', views.signOut, name='signout'),
    path('settings/', views.settings, name='settings'),
    path('post/<str:pk>/', views.post_detail, name='post_detail'),
    path('delete-comment/<str:pk>/', views.deleteComment, name='delete-comment'),
]
