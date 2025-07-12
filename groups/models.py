from django.db import models
from chore_and_snore import settings
from users.models import CustomUser


class Group(models.Model):
    name = models.CharField(max_length=100)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               related_name='leading_groups')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_groups')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
