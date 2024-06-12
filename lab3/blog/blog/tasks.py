from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import time
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils import timezone
from .models import LongRunningOperation

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False,
    )

    operation = LongRunningOperation.objects.create(
        operation_name='Send Email Task',
        data=f'Subject: {subject}, message: {message}, Recipients: {recipient_list}',
        datetime=timezone.now(),
        result='Email sent successfully'
    )

    print(f'Operation saved: {operation.operation_name}, {operation.data}, {operation.result}, {operation.datetime}')

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'operations', {
            'type': 'send_status_update',
            'message': {
                'operation_name': operation.operation_name,
                'data': operation.data,
                'result': operation.result,
                'datetime': str(operation.datetime)
            }
        }
    )
    print('WebSocket message sent')

@shared_task
def long_running_task(operation_data):

    operation = LongRunningOperation.objects.create(
        operation_name='Long Running Task',
        data=operation_data,
        datetime=timezone.now()
    )

    time.sleep(10)

    operation.result = f'Completed with data: {operation_data}'
    operation.save()

    print(f'Operation saved: {operation.operation_name}, {operation.data}, {operation.result}, {operation.datetime}')

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'operations', {
            'type': 'send_status_update',
            'message': {
                'operation_name': operation.operation_name,
                'data': operation.data,
                'result': operation.result,
                'datetime': str(operation.datetime)
            }
        }
    )
    print('WebSocket message sent')