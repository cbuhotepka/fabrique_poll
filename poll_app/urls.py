from django.urls import path, include
from .views import AllPollsView, QuestionDetailAPIView, AllQuestionListAPIView, AvailableQuestionListAPIView, AnsweredQuestionListAPIView, AnsweredQuestionDetailedListAPIView, AnswerAPIView

app_name = 'poll_app'
urlpatterns = [
    path('', AllPollsView.as_view(), name='available_polls'),

    # API paths
    path('api/all_questions', AllQuestionListAPIView.as_view()),
    path('api/answers_of_user/<int:pk>', AnsweredQuestionListAPIView.as_view()),

    path('api/answer', AnswerAPIView.as_view()),
    path('api/available_questions', AvailableQuestionListAPIView.as_view()),
    path('api/my_answers', AnsweredQuestionDetailedListAPIView.as_view()),
    path('api/question/<int:pk>', QuestionDetailAPIView.as_view()),
]
