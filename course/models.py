from django.db import models


class Subject(models.Model):
    Name = models.CharField(max_length=100)
    Question_Paper = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Number_Of_Questions = models.IntegerField(default=0)
    def __str__(self):
        return self.Name

class Enrolled(models.Model):
    Name = models.OneToOneField('users.StudentInfo',primary_key = True,on_delete=models.CASCADE)
    Subect =models.OneToOneField(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name.Name

class Teaches(models.Model):
    Name = models.OneToOneField('users.TeacherInfo',primary_key = True,on_delete=models.CASCADE)
    Subject =models.OneToOneField(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name.Name

class Marks(models.Model):
    Name = models.ForeignKey('users.StudentInfo',on_delete=models.CASCADE)
    Checker = models.ForeignKey('users.TeacherInfo',on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    Question_No = models.CharField(max_length=4)
    Marks = models.IntegerField()

    def __str__(self):
        return self.Name.Name
