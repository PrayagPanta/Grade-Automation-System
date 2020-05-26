from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,UpdateView
from .models import Marks,Subject,Teaches
from users.models import StudentInfo,TeacherInfo
from django.contrib.auth.decorators import login_required
from .forms import NameForm,AddForm,NameForm2,UpdateForm
import os
#from mlmodel import analyze
# Create your views here.

files = []
@login_required
def newRecord(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            SID = form.cleaned_data.get('SID')
            try:
                users = User.objects.get(id=SID)
                if( users.profile.role == 'T'):
                    return render(request,'course/courseDoesNotExist.html')
            except:
                return render(request,'course/courseDoesNotExist.html')
            return redirect(addMarks,SID)
        else:
            return render(request,'course/Error.html')
    else:
        if( request.user.profile.role == 'T'):
            form = NameForm()
            return render(request, 'course/newRecord.html', {'form': form})
        else:
            return render(request,'course/Error.html')

@login_required
def searchRecord(request):
    if request.method == 'POST':
        form = NameForm2(request.POST)
        if form.is_valid():
            sid =  form.cleaned_data.get('SID')
            qno = form.cleaned_data.get('Qno')
        try:
            users = User.objects.get(id=sid)
        except User.DoesNotExist:
            return render(request,'course/courseDoesNotExist.html')
        if( users.profile.role == 'T'):
            return render(request,'course/Error.html')
        return redirect(UpdateMarks,sid,qno,users)
    else:
        if( request.user.profile.role == 'T'):
            form = NameForm2()
            return render(request, 'course/searchRecord.html', {'form': form})
        else:
            return render(request,'course/Error.html')

@login_required
def addMarks(request,SID):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.Name = StudentInfo.objects.get(Sid=SID)
            obj.Checker = TeacherInfo.objects.get(Tid=request.user.id)
            obj.Subject = Teaches.objects.get(Name=obj.Checker).Subject
            obj.Question_No = form.cleaned_data.get('Qno')
            obj.save()
            # if else condition to check if there are unmarked questions present
            return render(request,'course/done.html')
        else:
            return render(request,'course/Error.html')
    elif request.method == 'GET':
        form = AddForm()
        Subject = Teaches.objects.get(Name=TeacherInfo.objects.get(Tid=request.user.id) ).Subject
        id = SID
        # if files is empty put each and every content of the directory in the file
        # else
        url = 'media/answersheet/'+str(id)+'/'+str(Subject)
        files = os.listdir(url)
        imgurl="/media/answersheet/"+str(id)+"/"+str(Subject)+"/1.jpg"
        # summary , marks, totalmarks = analyze(imgurl)
        return render(request, 'course/addMarks.html', {'form': form,'imgurl':imgurl,'files':files})
    else:
        pass
@login_required
def UpdateMarks(request,sid,qno,users):
    if request.method == 'GET':
        form = UpdateForm()
        marks = Marks.objects.filter(Question_No=qno,Subject=Teaches.objects.get(Name=TeacherInfo.objects.get(Tid=request.user.id) ).Subject,Name=sid).first()
        return render(request,'course/update.html',{'form': form ,'marks':marks.Marks})
    else:
        form = UpdateForm(request.POST)
        if form.is_valid():
            NewMarks =  form.cleaned_data.get('NewMarks')
            Marks.objects.filter(Question_No=qno,Subject=Teaches.objects.get(Name=TeacherInfo.objects.get(Tid=request.user.id) ).Subject,Name=sid).update(Marks=NewMarks)
            return render(request,'course/done2.html',{'NewMarks': NewMarks})
        else:
            return render(request,'course/Error.html')



#class PostCreateView(LoginRequiredMixin, CreateView):
#    model = Post
#    fields = ['title', 'content']

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)
