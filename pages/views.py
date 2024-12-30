from django.db.models.base import Model as Model
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"
