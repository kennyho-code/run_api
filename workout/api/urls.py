from django.conf.urls import url
from .views import WorkoutListAPIView

urlpatterns = [
    url('', WorkoutListAPIView.as_view(), name='workouts')

]