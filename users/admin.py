from django.contrib import admin
from .models import Profile,StudentInfo,TeacherInfo,Complaint
from django.contrib.auth.models import User


admin.site.register(Profile)
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
admin.site.register(Complaint)
#admin.site.register(CorrectsAnsof)
