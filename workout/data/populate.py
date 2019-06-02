import os
import django
import sys
sys.path.append('/Users/kennyho/dev/projects/run/run_api/run_api/run_api')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'run_api.settings')
django.setup()
from workout.models import Workout
from datetime import datetime
import json


def create_workout():
    with open('running.json', 'r') as file:
        json_rows = json.load(file)
        for row in json_rows:
            try:
                creationdate = datetime.strptime(row['creationdate'], '%Y-%m-%d %X %z')
                Workout.objects.get(creationdate=creationdate)
            except Workout.DoesNotExist:
                creationdate = None
            if creationdate:
                continue
            row['creationdate'] = datetime.strptime(row['creationdate'], '%Y-%m-%d %X %z')
            row['startdate'] = datetime.strptime(row['startdate'], '%Y-%m-%d %X %z')
            row['enddate'] = datetime.strptime(row['enddate'], '%Y-%m-%d %X %z')
            w = Workout(
                workoutactivitytype=row['workoutactivitytype'],
                duration=row['duration'],
                durationunit=row['durationunit'],
                totaldistance=row['totaldistance'],
                totaldistanceunit=row['totaldistanceunit'],
                totalenergyburned=row['totalenergyburned'],
                totalenergyburnedunit=row['totalenergyburnedunit'],
                sourcename=row['sourcename'],
                sourceversion=row['sourceversion'],
                creationdate=row['creationdate'],
                startdate=row['startdate'],
                enddate=row['enddate'],
            )
            w.save()





if __name__ == '__main__':
    print('Populating running workouts...')
    create_workout()
    print('Finished running workouts...')


