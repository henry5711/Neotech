from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, TypeUser, TypeCourse, Course, Lesson, ProgressUser, CourseUser, Exam, Question, DetailExam, ExamUser

@admin.register(TypeUser)
class TypeUserAdmin(admin.ModelAdmin):
    list_display = ['tipo']
    # Puedes agregar más configuraciones según tus necesidades

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'last_name', 'document', 'user_type']
    search_fields = ['user__username', 'name', 'last_name', 'document']

@admin.register(TypeCourse)
class TipeCourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type_course')
    search_fields = ('name', 'description')
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'content_html')
    search_fields = ('name',)
    

@admin.register(ProgressUser)
class ProgressUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'progress')
    search_fields = ('user__username', 'lesson__name')
    

@admin.register(CourseUser)
class CourseUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user__username', 'course__name')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'point')
    search_fields = ('course__name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_answer')
    search_fields = ('question', 'correct_answer')

@admin.register(DetailExam)
class DetailExamAdmin(admin.ModelAdmin):
    list_display = ('exam', 'question')
    search_fields = ('exam__course__name', 'question__question')

@admin.register(ExamUser)
class ExamUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'exam', 'date')
    search_fields = ('user__username', 'exam__course__name')


