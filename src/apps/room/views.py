from django.views.generic.edit import CreateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from src.forms.room.forms import FormRoom
from src.models.room.models import Room
from django.utils.text import slugify
from django.contrib.auth.hashers import check_password


class DeleteRoom(DeleteView):
    model           = Room
    template_name   = 'room/delete.html'
    success_url     = reverse_lazy('main:main_page')


class CreateRoom(CreateView):
    queryset        = Room.objects.all()
    form_class      = FormRoom
    template_name   = 'room/create.html'

    def form_valid(self, form):
        form.instance.founder   = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)



class CheckPassowrd(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'room/check_password.html', {})

    def post(self, request, *args, **kwargs):
        room        = Room.objects.get(pk=kwargs.get('pk'))
        slug        = slugify(room.name)
        password    = request.POST.get('password')
        if check_password(password, room.password):
            room.participants.add(request.user)
            return redirect(reverse('main:room:detail_room', kwargs={'slug': slug, 'pk': room.pk}))
        return redirect('main:main_page')



class DetailtRoom(View):

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=kwargs.get('pk'))
        slug = slugify(room.name)
        if self.request.user == room.founder or self.request.user in room.participants.all():
            return render(request, 'room/detail.html', {'room': room})
        else:
            return redirect(reverse('main:room:checkpassword', kwargs={'slug': slug, 'pk': room.pk}))
