from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.text import slugify


class Room(models.Model):
    ''' Модель создания комнаты  '''
    founder         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='founder_room')
    name            = models.CharField(max_length=255, blank=False)
    password        = models.CharField(max_length=255, blank=False)
    participants 	= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_in_room')
    create_date     = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        slug = slugify(self.name)
        return reverse('main:room:detail_room', kwargs={'slug': slug, 'pk': self.pk})

    def get_delete_room(self):
        slug = slugify(self.name)
        return reverse('main:room:delete_room', kwargs={'slug': slug, 'pk': self.pk})


    def __str__(self):
        return f"Комната {self.name}"


    class Meta:
        ordering = ['-create_date']
