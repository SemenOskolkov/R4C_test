from django.urls import path

from robots.views import *
from robots.apps import RobotsConfig

app_name = RobotsConfig.name

urlpatterns = [
    path('fill_robots_json/', fill_robots_json, name='fill_robots_json'),
    path('freport_robot_excel/', report_robot_excel, name='report_robot_excel'),
]
