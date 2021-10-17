from celery import shared_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from datetime import date, timedelta

from movies.models import Movie

logger = get_task_logger(__name__)

startdate = date.today()
enddate = startdate + timedelta(days=1)
movies = Movie.objects.filter(creat_timestamp__range=[startdate, enddate])

recievers = []
for user in User.objects.all():
    recievers.append(user.email)


@shared_task
def schedule_mail():
    # logger.info("The sample task just ran.")

    message = movies
    mail_subject = 'latest movies in the past day'
    to_email = recievers
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
