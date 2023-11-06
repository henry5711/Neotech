from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TipeCourse(models.Model):
    name=models.CharField(max_length=255, unique=True)
    
class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    tipe_course=models.ForeignKey(TipeCourse,on_delete=models.CASCADE)
class Lesson(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
        
class ProgressUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    progress=models.BooleanField(default=False)
    
class CourseUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    
class Exam(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    point=models.IntegerField(null=True)
    
class Question(models.Model):
    question=models.CharField(max_length=255)
    correct_answer=models.CharField(max_length=255)
    answer_1=models.CharField(max_length=255)
    answer_2=models.CharField(max_length=255)
    answer_3=models.CharField(max_length=255)
class DetailExam(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    
class ExamUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    


    