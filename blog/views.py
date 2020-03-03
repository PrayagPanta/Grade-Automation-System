from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from course.models import Enrolled
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if( request.user.profile.role == 'S'):
        return render(request, 'blog/student.html',{'title':'Home Page'})
    else:
        return render(request, 'blog/teacher.html',{'title':'Home Page'})

@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#class ViewEnrollment(ListView,LoginRequiredMixin):
    #model =  Enrolled
