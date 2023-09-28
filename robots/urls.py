from django.urls import path

from robots.views import *
from robots.apps import RobotsConfig

app_name = RobotsConfig.name

urlpatterns = [
    path('fill_robots_json/', fill_robots_json.as_view(), name='fill_robots_json'),
    path('freport_robot_excel/', report_robot_excel.as_view(), name='report_robot_excel'),
]
