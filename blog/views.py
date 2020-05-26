from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from course.models import Enrolled
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm

@login_required
def home(request):
    if( request.user.profile.role == 'S'):
        return render(request, 'blog/student.html',{'title':'Home Page'})
    else:
        return render(request, 'blog/teacher.html',{'title':'Home Page'})

@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def comp(request):
    return render(request,'blog/complaint_teacher.html')
@login_required
def compS(request):
    if request.method == 'GET':
        form = ComplaintForm()
        return render(request,'blog/complaint_student.html',{'form': form})
    else:
        return render(request,'blog/Noresults.html')

#class ViewEnrollment(ListView,LoginRequiredMixin):
    #model =  Enrolled
