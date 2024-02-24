from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_warden = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        # However in some cases, you might want to use your own custom user model, which is more flexible and can include additional fields.
        swappable = 'AUTH_USER_MODEl'


class Location(models.Model):
    loc_name = models.CharField(max_length=255)

    def __str__(self):
        return self.loc_name


class Hostel(models.Model):
    name = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    parent_name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Room(models.Model):
    BED_CHOICES = [
        ('single', 'Single Bed'),
        ('double', 'Double Bed'),
    ]

    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
    bed_type = models.CharField(max_length=10, choices=BED_CHOICES, default='single')

    def __str__(self):
        return self.room_number



