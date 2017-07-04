from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Team(models.Model):
    teamdescription = models.CharField(max_length=200)
    teamtypechoices = (('Research', 'Research'), ('Development', 'Development'))
    teamtype = models.CharField(
        max_length=11,
        choices=teamtypechoices,
        default='Development',)
    group = models.OneToOneField(
       Group,
       on_delete=models.CASCADE,
       primary_key=True)

    def countusers(self):
        return self.group.user_set.count()

    def allmembers(self):
        return self.group.user_set.order_by('username')
