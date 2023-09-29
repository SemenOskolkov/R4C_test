from django.conf import settings
from django.core.mail import send_mail


def generate_letter_and_send_mail(email_addresses, model, version):
    '''Генерация письма и отпавка email'''
    send_mail(
        subject=f'Робот модели {model}, версии {version} в наличии',
        message=f'Добрый день!\nНедавно вы интересовались нашим роботом модели {model}, версии {version}. Этот робот теперь в наличии.\nЕсли вам подходит этот вариант - пожалуйста, свяжитесь с нами.',
        recipient_list = email_addresses,
        from_email=settings.EMAIL_HOST_USER
    )