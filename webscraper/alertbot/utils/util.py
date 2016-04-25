import uuid
from django.utils import timezone
import requests
import json
from alertbot.utils.constants import Constant
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from random import randint

def getotp():
    return str(randint(100001, 999998))

def send_sms(number, message):
    url = Constant.SMS_URL.replace('TEXT_HERE', message)
    url = url.replace('MOBILE_HERE', number)
    return requests.get(url)

def send_email(email, subject, body):
    mail = EmailMultiAlternatives(subject, body, settings.EMAIL_USER, [email])
    return mail.send()
