Для решения задачи применил с модели **Robot** сигнал **post_save**
'''
from django.db.models.signals import post_save
'''
Чтобы код был более структурированным, решил разделить работу на 2 части:
1. В файле **robots/models.py** происходит работа с сигналом на сохранеие модели и проверки количества роботов. При условии что сигнал на отпраку письма происходит, если значение quantity > 0 и предыдущее значение quantity было равно 0.
2. В файле **oders/service.py** происходит генерация письма и отпрака его через email покупателю.

Для работы с отправкой email добавил в файл settings.py настройки почты и перенес их переменные окружения.