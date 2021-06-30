from django.db.models.fields import CharField
from rest_framework import serializers
from .models import Question, Answer, User, UserAnswer, Poll
from django.shortcuts import get_object_or_404


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=False)

    class Meta:
        model = Answer
        fields = ['id', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'type', 'answers', 'poll']

    def update(self, question_inst, validated_data):
        question_inst.question = validated_data.get('question', question_inst.question)
        question_inst.type = validated_data.get('type', question_inst.type)
        question_inst.poll = validated_data.get('poll', question_inst.poll)

        answers = validated_data.get('answers')
        question_inst.answers.clear()
        for answer in answers:
            answer_id = answer.get('id', None)
            if answer_id:
                answer_inst = Answer.objects.get(id=answer_id)
                answer_inst.question = question_inst
                answer_inst.answer = answer.get('answer', answer_inst.answer)
                answer_inst.save()
            else:
                answer_inst = Answer.objects.create(question=question_inst, **answer)
            question_inst.answers.add(answer_inst)
        
        print(question_inst.answers.all())
        question_inst.save()

        return question_inst


class PollDetailedSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    
    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'questions']


class UserAnswerDetailedSerializer(serializers.ModelSerializer):
    # question = serializers.StringRelatedField()
    choice_answers = serializers.SlugRelatedField(many=True, source='answers', slug_field='answer', read_only=True)
        
    class Meta:
        model = UserAnswer
        fields = ['choice_answers', 'text_answer']
        
    def get_queryset(self):
        user = User.objects.filter(session_key=self.request.session.session_key).first()
        queryset = UserAnswer.objects.filter(user=user)
        return queryset


class AnsweredQuestionSerializer(serializers.ModelSerializer):
    answer = UserAnswerDetailedSerializer(many=True, source='answered_questions', read_only=True)

    class Meta:
        model = Question
        fields = ['question', 'answer']



class AnsweredPollSerializer(serializers.ModelSerializer):
    questions = AnsweredQuestionSerializer(many=True)
    
    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'questions']


class PollUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Poll
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'questions']

    def update(self, poll_inst, validated_data):
        poll_inst.name = validated_data.get('name', poll_inst.name)
        poll_inst.description = validated_data.get('description', poll_inst.description)
        poll_inst.end_date = validated_data.get('end_date', poll_inst.end_date)
        questions = validated_data.get('questions', None)
        poll_inst.questions.set(questions)
        print(questions)
        poll_inst.save()

        # questions = validated_data.get('questions')

        return poll_inst


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['user_id', 'question_id', 'answers', 'text_answer']


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
