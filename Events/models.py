
from django.db import models

# Create your models here.
from django.db.models import Sum

from Users.models import users


class Event(models.Model):

    event_name = models.CharField(max_length=50)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    registration_closing_date = models.DateTimeField(auto_now_add=False)
    stage_name = models.CharField(max_length=20)

    def __str__ (self):
        return self.event_name


class Registration(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.event_name)+ " "+ str(self.user_id)




class Winner(models.Model):
    rid = models.ForeignKey(Registration, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(null=True)
    points = models.PositiveIntegerField(null=True)

    def __str__(self):
        return "Event : "+str(self.rid) +str(self.position)

    @classmethod
    def get_house_points(cls):
        return cls.objects.values('rid__user_id__student_house').annotate(Sum('points')).order_by('-points')
