from django.db import models
from django.contrib.auth.models import AbstractUser, User

class ImageList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    response_codes = models.JSONField()  # A list of response codes
    image_links = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('moderator', 'Moderator'),
    ]
    email = models.EmailField('Email Address', unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
    )

    class Meta:
        permissions = [
            ('can_view_customuser', 'Can view custom user'),
            ('can_add_customuser', 'Can add custom user'),
            ('can_change_customuser', 'Can change custom user'),
            ('can_delete_customuser', 'Can delete custom user'),
        ]