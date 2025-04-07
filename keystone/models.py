from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Building(models.Model):
    TZ_CHOICES = [('Asia/Beirut', 'Asia/Beirut'), ('Asia/Bishkek', 'Asia/Bishkek'), ('Asia/Brunei', 'Asia/Brunei'), ('Asia/Kolkata', 'Asia/Kolkata')]
    name = models.CharField(max_length=100)
    address = models.TextField()
    time_format_12h = models.BooleanField(default=False)
    timezone = models.CharField(max_length=100, choices=TZ_CHOICES, default='Asia/Kolkata')

    def __str__(self):
        return self.name


class Space(models.Model):
    SPACE_CHOICES = [('Room', 'Room'), ('Hall', 'Hall'), ('Office', 'Office')]
    name = models.CharField(max_length=100)
    space_type = models.CharField(max_length=100, choices=SPACE_CHOICES, default='Room')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='building')
    num_of_floor = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='devices')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='devices')
    floor = models.IntegerField()
    disable_adhoc_booking = models.BooleanField(default=False)
    meeting_confirmation = models.BooleanField(default=False)
    shoe_meeting_title = models.BooleanField(default=False)
    show_meeting_organizer = models.BooleanField(default=False)
    enable_scheduling = models.BooleanField(default=False)
    pin_required = models.BooleanField(default=False)

    def clean(self):
        # Only validate if space is set
        if self.space and self.floor > self.space.num_of_floor:
            raise ValidationError({
                'num_of_floor': f'Cannot be greater than total floors in space ({self.space.num_of_floor}).'
            })
    def __str__(self):
        return self.name

class NFC(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name