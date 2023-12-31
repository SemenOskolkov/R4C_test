Для решения задачи сначала добавил в модель Robot значение "quantity" и применил миграции.
для работы с Excel-файлом использовал библиотеку **openpyxl**
Чтобы код был более структурированным, решил разделить работу на 2 части:
1. В файле **robots/service.py** происходит генерация файла в формате Excel.
Конченой датой для составления отчета была использована дата на момент создания отчета, а начальной дельта в 7 дней.
При получении всех моделей роботов происходит обработка по необходимым показателям и суммированием значений "quantity".
'''
data = Robot.objects.filter(
            model=robot.model,
            version=robot.version,
            created__gte=start_date,
            created__lte=end_date
        ).aggregate(total_quantity=robots.Sum('quantity'))
'''
Также при создании отчета происходит запись данных на отдельный страницах каждой модели роботов.
'''
ws = wb.create_sheet(title=f'{robot.model}')
'''
2. В файле **robots/views.py** функуия **report_robot_excel** создает и отправляет файл в формате Excel.