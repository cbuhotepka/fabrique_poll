from django.urls import path, include
from .views import AllQuestionListAPIView, AnsweredPollsListAPIView
from .views import QuestionDetailAPIView, QuestionUpdateAPIView, QuestionCreateAPIView
from .views import AnswerAPIView
from .views import AllPollsView, PollDetailAPIView, PollUpdateAPIView, PollCreateAPIView, AvailablePollsListAPIView, UserAnsweredPollsListAPIView

app_name = 'poll_app'
urlpatterns = [
    path('', AllPollsView.as_view(), name='available_polls'),

    # API paths
    path('api/all_questions', AllQuestionListAPIView.as_view()),

    path('api/question_detail/<int:pk>', QuestionDetailAPIView.as_view()),
    path('api/question_update/<int:pk>', QuestionUpdateAPIView.as_view()),
    path('api/question_create', QuestionCreateAPIView.as_view()),

    path('api/poll_detail/<int:pk>', PollDetailAPIView.as_view()),
    path('api/poll_update/<int:pk>', PollUpdateAPIView.as_view()),
    path('api/poll_create', PollCreateAPIView.as_view()),

    path('api/answer', AnswerAPIView.as_view()),
    path('api/my_answers', AnsweredPollsListAPIView.as_view()),

    path('api/available_polls', AvailablePollsListAPIView.as_view()),
    path('api/answers_of_user/<int:pk>', UserAnsweredPollsListAPIView.as_view()),
]
