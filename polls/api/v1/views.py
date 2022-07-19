from rest_framework.viewsets import ModelViewSet

from polls.api.v1.serializers import ChoiceSerializer, QuestionSerializer
from polls.models import Choice, Question


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ChoiceViewSet(ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
