from rest_framework import generics
from workout.models import Workout
from .serializers import WorkoutSerializer

class WorkoutListAPIView(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get(self, request, *args, **kwargs):
        print(self.queryset[0].creationdate)
        return self.list(request, *args, **kwargs)


