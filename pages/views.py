from typing import Any
from django.db.models.base import Model as Model
from django.http.response import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin

from core.forms import LinkForm
from core.models import Link, UserLinkCategory


class HomeView(TemplateView):
    template_name = "pages/home.html"
    model = Link

    def get(self, request):
        if request.user.is_authenticated:
            non_deleted_links = (
                Link.objects.all()
                .filter(deleted_at=None)
                .filter(created_by=request.user)
            )
            return render(
                request, self.template_name, {"non_deleted_links": non_deleted_links}
            )
        return render(request, self.template_name)


@method_decorator(login_required, name="dispatch")
class LinkView(TemplateView):
    template_name = "pages/link.html"

    def get(self, request, link_id):
        link = get_object_or_404(Link, uuid=link_id)
        return render(request, self.template_name, {"link": link})


@method_decorator(login_required, name="dispatch")
class LinkCreateView(CreateView):
    template_name = "pages/link_create.html"
    model = Link
    form_class = LinkForm

    def get_success_url(self) -> str:
        return reverse("home")

    def form_valid(self, form):
        custom_category = form.cleaned_data.get("custom_category")

        if custom_category:
            # Check if the user has a category with the same name
            category = UserLinkCategory.objects.filter(
                user=self.request.user, name=custom_category
            ).first()
            if category:
                form.instance.category = category
            else:
                # Create a new UserLinkCategory if a custom category is provided
                category = UserLinkCategory.objects.create(
                    user=self.request.user, name=custom_category
                )
            form.instance.category = category  # Assign the newly created category

        form.instance.created_by = self.request.user
        messages.success(self.request, "Link saved successfully")
        return super(LinkCreateView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class LinkEditView(UserPassesTestMixin, UpdateView):
    template_name = "pages/link_edit.html"
    model = Link
    form_class = LinkForm

    def test_func(self) -> bool:
        return self.get_object().created_by == self.request.user

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(
            self.request,
            "You are not the creator of this job, please login with the correct account",
        )
        return redirect("home")

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return Link.objects.get(uuid=self.kwargs["link_id"])

    def form_valid(self, form):
        custom_category = form.cleaned_data.get("custom_category")

        if custom_category:
            # Check if the user has a category with the same name
            category = UserLinkCategory.objects.filter(
                user=self.request.user, name=custom_category
            ).first()
            if category:
                form.instance.category = category
            else:
                # Create a new UserLinkCategory if a custom category is provided
                category = UserLinkCategory.objects.create(
                    user=self.request.user, name=custom_category
                )
            form.instance.category = category  # Assign the newly created category

        form.instance.created_by = self.request.user
        messages.success(self.request, "Link saved successfully")
        return super(LinkEditView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse("link", kwargs={"link_id": self.kwargs["link_id"]})


class LinkDeleteView(DeleteView):
    model = Link
    template_name = "pages/link_delete.html"

    def test_func(self) -> bool:
        return self.get_object().created_by == self.request.user

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(
            self.request,
            "You are not the creator of this job, please login with the correct account",
        )
        return redirect("home")

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return Link.objects.get(uuid=self.kwargs["link_id"])

    def get_success_url(self) -> str:
        return reverse("home")
