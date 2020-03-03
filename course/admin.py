from django.contrib import admin
from .models import Subject,Enrolled,Teaches,Marks
# Register your models here.

admin.site.register(Subject)
admin.site.register(Enrolled)
admin.site.register(Teaches)
admin.site.register(Marks)
