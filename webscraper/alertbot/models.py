from __future__ import unicode_literals
import uuid
from django.db import models
from django.utils import timezone
from django.core.validators import validate_email, MinLengthValidator, RegexValidator
from alertbot.utils import util
from alertbot.utils.file_validator import FileValidator

validate_file = FileValidator(max_size=1024 * 3000,
                             content_types=('image/png','image/jpeg','image/jpg',))

name_regex = RegexValidator(r'^[a-zA-Z _.-]*$', 'Only Alphabets with (._-) are allowed.')
number_regex = RegexValidator(r'^[789]\d{9}$', 'Invalid mobile number.')

def get_random_token():
    return str(uuid.uuid1())
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3), name_regex])
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=254, unique=True, db_index=True, validators=[validate_email])
    mobile = models.CharField(max_length=10, unique=True, db_index=True, validators=[MinLengthValidator(10), number_regex])
    otp = models.CharField(max_length=10, default=util.getotp)
    activated = models.BooleanField(default=False)
    image = models.FileField(upload_to='images', default='', validators=[validate_file])

# class Session(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     key = models.CharField(default = get_random_token, max_length=500)
#     ttl = models.DateTimeField(default=(timezone.now() + timezone.timedelta(seconds=600)))


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    act_price = models.CharField(max_length=10, default="0")
    exp_to = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exp_from = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    url = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)

    def as_json(self):
        alert = {
            "name": self.name,
            "id": self.id,
            "act_price": self.act_price,
            "url": self.url
        }
        return alert

    def for_scheduling(self):
        alert = {
            "name": self.name,
            "id": self.id,
            "act_price": self.act_price,
            "url": self.url,
            "exp_to": self.exp_to,
            "exp_from": self.exp_from
        }
        return alert
