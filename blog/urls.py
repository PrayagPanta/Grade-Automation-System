from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('complaints/',views.comp,name='comp'),
    path('compS/',views.compS,name='compS')
]
