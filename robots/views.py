import json
from django.http import JsonResponse
from django.shortcuts import render

from robots.models import Robot
from robots.service import generate_robot_summary
from django.http import HttpResponse


def fill_robots_json(request):
    '''Заполнение таблицы robot в базу данных через json'''
    if request.method == 'POST':
        try:
            data_json = json.loads(request.body)
            serial = model + "-" + version
            model = data_json['model']
            version = data_json['version']
            quantity = data_json['quantity']
            created = data_json['created']
            robot = Robot(serial=serial, model=model, version=version, quantity=quantity, created=created)
            robot.save()
            return JsonResponse(
                {'message': 'Robot created successfully'},
                status=201)
        except:
            return JsonResponse(
                {'massage': 'Invalid data format'},
                status=400)
    else:
        return JsonResponse(
            {'massage': 'Invalid request method'},
            status=405)
        
        
def report_robot_excel(request):
    generate_robot_summary(response)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=robot_summary.xlsx'
    return response
