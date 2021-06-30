from django.contrib import admin
from .models import Question, Answer, User, UserAnswer, Poll
from django.conf import settings

# Register your models here.
admin.site.register(Answer)
admin.site.register(User)
# admin.site.register(Poll)

if settings.DEBUG:
    admin.site.register(UserAnswer)

class AnswersInline(admin.TabularInline):
    model = Answer
    list_display = ['answer']
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    list_display = ['question']
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswersInline, )

@admin.register(Poll)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuestionInline, )