from django.dispatch import receiver
from django.db.models.signals import pre_save
from accounts.models import Profile
import os


@receiver(pre_save, sender=Profile)
def del_old_photo(sender, instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_photo = sender.objects.get(id=instance.pk)
    except sender.DoesNotExist:
        return False

    if old_photo.photo and instance.photo:
        file = instance.photo
        if not old_photo.photo == file:
            if os.path.isfile(old_photo.photo.path):
                os.remove(old_photo.photo.path)
