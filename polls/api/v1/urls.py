from multiprocessing.spawn import import_main_path
from rest_framework.routers import DefaultRouter
from polls.api.v1.views import ChoiceViewSet, QuestionViewSet


router = DefaultRouter(trailing_slash=True)

router.register("questions", QuestionViewSet)
router.register("choices", ChoiceViewSet)

urlpatterns = router.urls
