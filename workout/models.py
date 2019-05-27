from django.db import models

class Workout(models.Model):
    creationdate = models.DateTimeField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    sourcename = models.CharField(max_length=64)
    sourceversion = models.CharField(max_length=64)
    totaldistance = models.FloatField()
    totaldistanceunit = models.CharField(max_length=64)
    duration = models.FloatField()
    durationunit = models.CharField(max_length=64)
    totalenergyburned = models.FloatField()
    totalenergyburnedunit = models.CharField(max_length=64)
    workoutactivitytype = models.CharField(max_length=64)