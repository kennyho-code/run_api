from lxml import html
from datetime import datetime
import json

def xml_to_json():
    xml_doc = open('export.xml', 'rb').read()
    page = html.fromstring(xml_doc)
    workouts = page.xpath('.//workout')
    # workouts = [dict(w.attrib) for w in workouts]
    with open('running.json', 'w') as json_file:
        res = []
        for workout in workouts:
            w = dict(workout.attrib)
            if w['workoutactivitytype'] != 'HKWorkoutActivityTypeRunning':
                continue
            # if not is_current_month(w['creationdate']):
            #     continue

            w['duration'] = float(w['duration'])
            w['totaldistance'] = float(w['totaldistance'])
            w['totalenergyburned'] = float(w['totalenergyburned'])
            res.append(w)
        json.dump(res, json_file)


def is_current_month(date_str):
    dt_obj = datetime.strptime(date_str, '%Y-%m-%d %X %z')
    curr_month = datetime.now().month
    if dt_obj.month == curr_month:
        return True
    return False


if __name__ == '__main__':
    xml_to_json()


