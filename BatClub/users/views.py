from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import  FormView
from .forms import RegisterForm


class RegisrerView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)