from django.urls import path
from . import views

urlpatterns = [
    path('newRecord/', views.newRecord, name='new-Record'),
    path('searchRecord/', views.searchRecord, name='search-Record'),
    path('addMarks/<int:SID>/',views.addMarks,name='add-Marks'),
    path('done/',views.done,name='done')
]
