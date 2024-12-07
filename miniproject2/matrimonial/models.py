from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length = 15)
    dob = models.DateField(default=datetime.date.today,verbose_name="Date of Birth")
    gender_options = [
        ('Male','Male'),
        ('Female','Female')
    ]
    gender = models.CharField(max_length=15, choices=gender_options, default='Male')
    height = models.FloatField(blank = True, null = True, help_text = "Height in centimeters")
    weight = models.FloatField(blank = True, null = True, help_text = "Weight in kilograms")
    profile_image = models.ImageField(upload_to = "static/images/profile/", blank = True,null = True)
    skin_choices = [
        ('Fair','Fair'),
        ('Medium','Medium'),
        ('Dark','Dark')
    ]
    skin_type = models.CharField(max_length = 15, choices = skin_choices, default = 'Fair')
    religion_choice = [
        ('Spritual','Spritual'),
        ('Buddhist','Buddhist'),
        ('Hindu','Hindu'),
        ('Christian','Christian'),
        ('Muslim','Muslim')
    ]
    religion_type = models.CharField(max_length=20, choices=religion_choice, default = 'Hindu')
    location_choice = [
        ('India', 'India'),
        ('Nepal', 'Nepal'),
        ('Bangladesh', 'Bangladesh'),
        ('Tibet', 'Tibet'),
        ('Bhutan', 'Bhutan')
    ]
    location_type = models.CharField(max_length=20, choices=location_choice, default = 'India')

class FriendRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    sender = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('sender', 'receiver')  # Prevent duplicate friend requests

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({self.status})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


# Create your models here.
