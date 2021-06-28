from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    QUESTION_TYPES = [
        ('single', 'Single choice'),
        ('multiple', 'Multiple choice'),
        ('text', 'Text answer'),
    ]
    type = models.CharField(max_length=32, choices=QUESTION_TYPES)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.name

    def clean(self):
        if self.type == 'text' and self.answer_set.all() :
            raise ValidationError("There cannot be choices in the text-answer type of the question")
        if self.end_date < datetime.date.today():
            raise ValidationError("End date cannot be less than start date")



class Answer(models.Model):
    answer = models.CharField(max_length=1024)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer


class User(models.Model):
    session_key = models.CharField(max_length=256)

    def __str__(self):
        return str(self.pk) + ' - ' + self.session_key


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers_of_user')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers_of_users')
    answers = models.ManyToManyField(Answer, blank=True)
    text_answer = models.CharField(max_length=1024, blank=True)

