from django.views.generic import TemplateView
from inventario.models import Genero, Editorial


# Create your views here.
class Home(TemplateView):
    template_name= "web/base.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['categorias'] = Genero.objects.all()
        context['editoriales'] = Editorial.objects.all()

        return context
        