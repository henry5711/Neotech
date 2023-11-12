from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#--------------------------------------------------------------------------------------#
# TipeUser - Tipo de Usuario#
class TypeUser(models.Model):
    TIPO_CHOICES = [
        ('superusuario', 'Superusuario'),
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
#--------------------------------------------------------------------------------------#
# UserProfile - Perfil de Usuario#
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    document = models.CharField(max_length=100, blank=True)
    user_type = models.ForeignKey(TypeUser, on_delete=models.CASCADE, default=3)  # 3 corresponds to 'estudiante'
#--------------------------------------------------------------------------------------#
#Tipe Course - Tipo de Curso#
class TypeCourse(models.Model):
    name=models.CharField(max_length=255, unique=True)
    
#--------------------------------------------------------------------------------------#
#Course - Curso#   
 
class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    type_course=models.ForeignKey(TypeCourse,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courseimages/', default='courseimages/default.png')

def __str__(self):
    return self.name
    
#--------------------------------------------------------------------------------------#
#lesson - leccion#

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content_html = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
def __str__(self):
    return self.name

#--------------------------------------------------------------------------------------#
#ProgressUser - Progreso de Usuario#
        
class ProgressUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    progress=models.BooleanField(default=False)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    
#--------------------------------------------------------------------------------------#
#CourseUser - Curso Usuario#
    
class CourseUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    
#--------------------------------------------------------------------------------------#
#Exam - Examen#
    
class Exam(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    point=models.IntegerField(null=True)
    
#--------------------------------------------------------------------------------------#
#Question - Pregunta#
    
class Question(models.Model):
    question = models.TextField()
    correct_answer = models.TextField()
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()

    def __str__(self):
        return self.question

    
#--------------------------------------------------------------------------------------#
#DetailExamn - Detalle de Examen#

class DetailExam(models.Model):
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    
#--------------------------------------------------------------------------------------#
#ExamenUser - Examen Usuario#
    
class ExamUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
        return f"{self.user.username} - {self.exam.name} - {self.date}"

    