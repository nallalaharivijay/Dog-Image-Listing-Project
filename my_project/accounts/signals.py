from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser

@receiver(post_migrate)
def create_custom_permissions(sender, **kwargs):
    if sender.name == 'accounts':  # Replace 'your_app_name' with your actual app name
        content_type = ContentType.objects.get_for_model(CustomUser)
        Permission.objects.create(
            codename='can_view_customuser',
            name='Can view custom user',
            content_type=content_type,
        )
        Permission.objects.create(
            codename='can_add_customuser',
            name='Can add custom user',
            content_type=content_type,
        )
        Permission.objects.create(
            codename='can_change_customuser',
            name='Can change custom user',
            content_type=content_type,
        )
        Permission.objects.create(
            codename='can_delete_customuser',
            name='Can delete custom user',
            content_type=content_type,
        )