from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, TypeUser

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        # Asignar el tipo de usuario "superusuario" (id=1)
        # Antes
        profile.user_type_id = 1  # Establecer a 1 para superusuario
        # Después
        profile.user_type_id = 3  # Establecer a 3 para "estudiante"
        profile.save()