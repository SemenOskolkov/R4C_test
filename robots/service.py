from django.utils import timezone
from openpyxl import Workbook

from robots.models import Robot


def generate_robot_summary(response):
    
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=7)
    
    robots = Robot.objects.all()
    
    wb = Workbook()
    for robot in robots:
        ws = wb.create_sheet(title=f'{robot.model}')
        ws.append(["Модель", "Версия", "Количество за неделю"])
        data = Robot.objects.filter(
            model=robot.model,
            version=robot.version,
            created__gte=start_date,
            created__lte=end_date
        ).aggregate(total_quantity=robots.Sum('quantity'))
        ws.append([robot.model, robot.version, data['total_quantity']])
        
    default_sheet = wb['Sheet']
    wb.remove(default_sheet)

    wb.save(response)

    
