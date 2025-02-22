# signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import Group
from apps.login.models import CustomUser

@receiver(m2m_changed, sender=Group.user_set.through)
def atribuir_is_staff(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == "post_add":
        grupo_desejado = Group.objects.get(name="Editor")
        if grupo_desejado in instance.groups.all():
            instance.is_staff = True
            instance.save()
