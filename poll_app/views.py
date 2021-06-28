from django.shortcuts import render
from django.views.generic import View
from .models import Question, User
import datetime
from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionSerializer, UserAnswerSerializer, UserAnswerDetailedSerializer, AnswerSerializer

def get_or_create_user(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    user = User.objects.filter(session_key=session_key).first()
    if not user:
        user = User(session_key=session_key).save()
    return user


# Create your views here.
class AllPollsView(View):
    template_name = 'poll_app/polls_list.html'

    def get(self, request):
        user = get_or_create_user(request)
        today = datetime.date.today()
        available_polls = Question.objects.filter(start_date__lte=today).filter(end_date__gte=today)
                
        context = {
            'user': user,
            'available_polls': available_polls,
        }
        return render(request, self.template_name, context)


# API Views
class QuestionDetailAPIView(APIView):
    serializer_class = QuestionSerializer

    def get(self, request, pk):
        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

        
class AllQuestionListAPIView(APIView):
    serializer_class = QuestionSerializer

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class AvailableQuestionListAPIView(APIView):
    serializer_class = QuestionSerializer

    def get(self, request):
        user = get_or_create_user(request)
        today = datetime.date.today()
        questions = Question.objects.filter(start_date__lte=today).filter(end_date__gte=today).prefetch_related('answers_of_users')
        questions = questions.exclude(answers_of_users__user=user)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class AnsweredQuestionDetailedListAPIView(APIView):
    serializer_class = UserAnswerDetailedSerializer

    def get(self, request):
        user = get_or_create_user(request)
        user_answers = user.answers_of_user
        serializer = UserAnswerDetailedSerializer(user_answers, many=True)
        return Response(serializer.data)


class AnsweredQuestionListAPIView(APIView):
    serializer_class = UserAnswerSerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user_answers = user.answers_of_user
        serializer = UserAnswerSerializer(user_answers, many=True)
        return Response(serializer.data)


class AnswerAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        if 'user_id' not in request.data:
            request.data['user_id'] = get_or_create_user(request).id
        answer = AnswerSerializer(data=request.data)
        print(answer)
        if answer.is_valid():
            answer.save()
            return Response({'result': 'ok'})
        return Response(answer.errors, status=status.HTTP_400_BAD_REQUEST)
