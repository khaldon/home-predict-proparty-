from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views
app_name = 'registration'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'), 
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('gallery/', views.GalleryPage.as_view(), name='gallery'),
    path('properties/',views.PropertiesPage.as_view(), name='properties'),
    path('properties-details/', views.PropertiesDetailPage.as_view(), name='properties-detail'),
    path('blog-archive/', views.BlogArchive.as_view(), name='blog-archive'),
    path('blog-predict-house/', views.BlogSingle.as_view(), name='predict-house'),
    
]   