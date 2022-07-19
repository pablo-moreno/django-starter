from polls.models import Question, Choice
from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "question", "choice_text", "votes", )
        read_only_fields = ("id", )


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date", "choices", )
        read_only_fields = ("id", "choices", )
