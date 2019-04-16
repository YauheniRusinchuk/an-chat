from django.views.generic.edit import CreateView, FormView
from src.forms.room.forms import FormRoom
from src.models.room.models import Room

class CreateRoom(CreateView):
    queryset        = Room.objects.all()
    form_class      = FormRoom
    success_url     = '/'
    template_name   = 'room/create.html'


    def form_valid(self, form):
        form.instance.founder   = self.request.user
        return super().form_valid(form)
