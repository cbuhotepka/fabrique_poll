from rest_framework import serializers
from .models import Question, Answer, User, UserAnswer
from django.shortcuts import get_object_or_404


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, source='answer_set')
    
    class Meta:
        model = Question
        fields = ['id', 'name', 'description', 'type', 'start_date', 'end_date', 'answers']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['user_id', 'question_id', 'answers', 'text_answer']


class UserAnswerDetailedSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    answer = AnswerSerializer(many=True)

    class Meta:
        model = UserAnswer
        fields = ['user_id', 'question', 'answers', 'text_answer']


class AnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    question_id = serializers.IntegerField()

    class Meta:
        model = UserAnswer
        fields = ['user_id', 'question_id', 'answers', 'text_answer']

    def is_valid(self):
        result = super().is_valid()
        question = get_object_or_404(Question, pk=self.validated_data.get('question_id'))
        existing_answer = UserAnswer.objects.filter(question=question).filter(user=self.validated_data.get('user_id')).first()
        if existing_answer:
            raise serializers.ValidationError('Answer already exists')
        answer = self.validated_data.get('answers')
        text_answer = self.validated_data.get('text_answer')
        
        if question.type == 'single':
            if text_answer:
                raise serializers.ValidationError("There shouldn't be text answer in a single-answer question")
            return result and len(answer) == 1 and not text_answer
        elif question.type == 'multiple':
            if text_answer:
                raise serializers.ValidationError("There shouldn't be text answer in a multi-answer question")
            return result and answer
        else:
            if answer:
                raise serializers.ValidationError("There shouldn't be option answer in a text-answer question")
            return result and text_answer
