from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    roles = [
        ('S', 'Student'),
        ('T', 'Teacher'),
    ]
    role = models.CharField(
        max_length=1,
        choices=roles,
        default='S'
      )

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username

class StudentInfo(models.Model):
    Sid = models.OneToOneField(Profile, primary_key=True,on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    School = models.CharField(max_length=80)
    Exam_Center = models.CharField(max_length=80)

    def __str__(self):
        return self.Name


class TeacherInfo(models.Model):
    Tid = models.OneToOneField(Profile, primary_key=True,on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    School = models.CharField(max_length=80)

    def __str__(self):
        return self.Name

class Complaint(models.Model):
    Sid = models.OneToOneField(StudentInfo, primary_key=True,on_delete=models.CASCADE)
    Tid = models.OneToOneField(TeacherInfo,on_delete=models.CASCADE)
    Subject = models.OneToOneField('course.Subject',on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=500)
