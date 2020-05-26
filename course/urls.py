from django.urls import path
from . import views

urlpatterns = [
    path('newRecord/', views.newRecord, name='new-Record'),
    path('searchRecord/', views.searchRecord, name='search-Record'),
    path('addMarks/<int:SID>/',views.addMarks,name='add-Marks'),
    path('searchRecord/UpdateMarks/<str:sid>/<str:qno>/<str:users>/',views.UpdateMarks,name='update-Marks'),
]
