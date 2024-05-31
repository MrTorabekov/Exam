from django.views.generic import ListView,DeleteView
from .models import Home


class HomeView(ListView):
    model = Home
    template_name = 'home.html'
    success_url = '/'
    context_object_name = 'homes'


class HomeDeleteView(DeleteView):
    model = Home
    pk_url_kwarg = 'pk'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

