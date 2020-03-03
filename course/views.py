from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,UpdateView
from .models import Marks,Subject,Teaches
from django.contrib.auth.decorators import login_required
from .forms import NameForm,AddForm
# Create your views here.
@login_required
def newRecord(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            SID = form.cleaned_data.get('SID')
            try:
                users = User.objects.get(id=SID)
            except User.DoesNotExist:
                return render(request,'course/courseDoesNotExist.html')
            return redirect(addMarks)
        else:
            return render(request,'course/Error.html')
    else:
        if( request.user.profile.role == 'T'):
            form = NameForm()
            return render(request, 'course/newRecord.html', {'form': form})
        else:
            return render(request,'Error.html')

@login_required
def searchRecord(request):
    if request.method == 'POST':
        pass
    else:
        if( request.user.profile.role == 'T'):
            form = NameForm()
            return render(request, 'course/searchRecord.html', {'form': form})
        else:
            return render(request,'Error.html')

@login_required
def addMarks(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.Name = request.GET
            obj.Checker = user.username
            obj.Subject = Teaches.objects.get(Name=user).subject
            obj.save()
        else:
            return render(request,'course/Error.html')
    elif request.method == 'GET':
        form = AddForm()
        return render(request, 'course/addMarks.html', {'form': form})
    else:
        pass
#class PostCreateView(LoginRequiredMixin, CreateView):
#    model = Post
#    fields = ['title', 'content']

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)
