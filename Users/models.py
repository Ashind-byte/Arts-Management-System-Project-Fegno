from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class users(AbstractUser):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    HOUSE = [
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Blue', 'Blue',)
    ]
    student_house = models.CharField(max_length=30, choices=HOUSE)
    gender = models.CharField(max_length=20, choices=GENDER)


    def save(self, **kwargs):
        if not self.is_superuser and not self.student_house:
            user_count = users.objects.filter(is_superuser= False).count() + 1
            mod = user_count % len(self.HOUSE)
            self.student_house = self.HOUSE[mod][0]
        if self.is_superuser is True:
            self.student_house=''

        super(users, self).save(**kwargs)
    def __str__(self):
        return self.first_name +" "+ self.last_name
