from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='/images/avatars/')
    user = models.ForeignKey(User, unique='True')
