from django.shortcuts import render
from django.views.generic import View
from .models import Question, User, Poll, UserAnswer
import datetime
from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionSerializer, UserAnswerSerializer, UserAnswerDetailedSerializer, AnswerSerializer
from .serializers import PollUpdateSerializer, PollDetailedSerializer, AnsweredPollSerializer
from django.db.models import Q
from django.db.models import Prefetch

def get_or_create_user(request):
    if not request.session.session_key:
        request.session.create()
        request.session.save()
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
        available_polls = Poll.objects.filter(start_date__lte=today).filter(end_date__gte=today)
                
        context = {
            'user': user,
            'available_polls': available_polls,
        }
        return render(request, self.template_name, context)


# API Views
class PollDetailAPIView(APIView):
    serializer_class = PollDetailedSerializer

    def get(self, request, pk):
        poll = Poll.objects.get(pk=pk)
        serializer = PollDetailedSerializer(poll)
        return Response(serializer.data)
        

class PollUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PollUpdateSerializer
    permission_classes = (IsAdminUser, )
    queryset = Poll.objects.all()    


class PollCreateAPIView(CreateAPIView):
    serializer_class = PollUpdateSerializer
    permission_classes = (IsAdminUser, )
    queryset = Poll.objects.all()


class AvailablePollsListAPIView(APIView):
    serializer_class = AnsweredPollSerializer

    def get(self, request):
        user = get_or_create_user(request)
        today = datetime.date.today()
        polls = Poll.objects.filter(start_date__lte=today).filter(end_date__gte=today).prefetch_related('questions__answers_of_users')
        polls = polls.exclude(questions__answers_of_users__user=user)
        serializer = AnsweredPollSerializer(polls, many=True)
        return Response(serializer.data)


class QuestionDetailAPIView(APIView):
    serializer_class = QuestionSerializer

    def get(self, request, pk):
        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class QuestionUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser, )
    queryset = Question.objects.all()


class QuestionCreateAPIView(CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser, )
    queryset = Question.objects.all()


class AllQuestionListAPIView(APIView):
    serializer_class = QuestionSerializer

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class AnsweredPollsListAPIView(APIView):
    serializer_class = AnsweredPollSerializer

    def get(self, request):
        user = get_or_create_user(request)
        user_answers = user.answers_of_user.all()
        for user_answer in user_answers:
            print(user_answer)
        prefetch = Prefetch('questions__answers_of_users', queryset=UserAnswer.objects.filter(user=user), to_attr='answered_questions')
        polls = Poll.objects.filter(questions__answers_of_users__in=user_answers).distinct().prefetch_related(prefetch)
        serializer = AnsweredPollSerializer(polls, many=True)
        return Response(serializer.data)


class UserAnsweredPollsListAPIView(APIView):
    serializer_class = AnsweredPollSerializer

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user_answers = user.answers_of_user.all()
        for user_answer in user_answers:
            print(user_answer)
        prefetch = Prefetch('questions__answers_of_users', queryset=UserAnswer.objects.filter(user=user), to_attr='answered_questions')
        polls = Poll.objects.filter(questions__answers_of_users__in=user_answers).distinct().prefetch_related(prefetch)
        serializer = AnsweredPollSerializer(polls, many=True)
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
