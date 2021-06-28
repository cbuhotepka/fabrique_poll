from django.contrib import admin
from .models import Question, Answer, User, UserAnswer

# Register your models here.
# admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)


class AnswersInline(admin.TabularInline):
    model = Answer
    list_display = ['answer']
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswersInline, )