from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import render, redirect, reverse
from src.forms.room.forms import FormRoom
from src.models.room.models import Room

class CreateRoom(CreateView):
    queryset        = Room.objects.all()
    form_class      = FormRoom
    template_name   = 'room/create.html'

    def form_valid(self, form):
        form.instance.founder   = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)



class DetailtRoom(View):

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=kwargs.get('pk'))
        if self.request.user == room.founder or self.request.user in room.participants.all():
            return render(request, 'room/detail.html', {'room': room})
        else:
            return redirect('main:main_page')
