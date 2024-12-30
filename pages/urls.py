from django.urls import path

from .views import HomeView, LinkCreateView, LinkView, LinkEditView, LinkDeleteView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("create_link/", LinkCreateView.as_view(), name="create_link"),
    path("link/<uuid:link_id>/", LinkView.as_view(), name="link"),
    path("link/<uuid:link_id>/edit/", LinkEditView.as_view(), name="link_edit"),
    path("link/<uuid:link_id>/delete/", LinkDeleteView.as_view(), name="link_delete"),
]
