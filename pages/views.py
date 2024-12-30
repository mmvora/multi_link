from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib import messages

from core.models import Link


class HomeView(TemplateView):
    template_name = "pages/home.html"


@method_decorator(login_required, name="dispatch")
class LinkCreateView(CreateView):
    template_name = "pages/new_link.html"
    model = Link
    fields = ["url", "title", "description"]

    def get_success_url(self) -> str:
        return reverse("home")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Link saved successfully")
        return super(LinkCreateView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class LinkView(TemplateView):
    template_name = "pages/link.html"

    def get(self, request, link_id):
        link = get_object_or_404(Link, uuid=link_id)
        return render(request, self.template_name, {"link": link})
