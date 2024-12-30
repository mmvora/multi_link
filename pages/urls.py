from django.urls import path

from .views import HomeView, LinkCreateView, LinkView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("new_link/", LinkCreateView.as_view(), name="new_link"),
    path("link/<uuid:link_id>/", LinkView.as_view(), name="link"),
]
