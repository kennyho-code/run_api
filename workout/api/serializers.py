from rest_framework import serializers


class WorkoutSerializer(serializers.Serializer):
    creationdate = serializers.DateTimeField()
    startdate = serializers.DateTimeField()
    enddate = serializers.DateTimeField()
    sourcename = serializers.CharField()
    sourceversion = serializers.CharField()
    totaldistance = serializers.FloatField()
    totaldistanceunit = serializers.CharField()
    duration = serializers.FloatField()
    durationunit = serializers.CharField()
    totalenergyburned = serializers.FloatField()
    totalenergyburnedunit = serializers.CharField()
    workoutactivitytype = serializers.CharField()

