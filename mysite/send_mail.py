import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':   

    send_mail(
        'your order has been confirmed',
        'your order has been confirmed',
        '903501845@qq.com',
        ['no_reply_myride@sina.com'],
        fail_silently=False
    )