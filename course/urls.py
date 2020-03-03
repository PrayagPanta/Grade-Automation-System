from django.urls import path
from . import views

urlpatterns = [
    path('newRecord/', views.newRecord, name='new-Record'),
    path('searchRecord/', views.searchRecord, name='search-Record'),
    path('addMarks/',views.addMarks,name='add-Marks'),
]
