from django.urls import path
from django.views.generic import TemplateView

app_name = "paslaugos"

urlpatterns = [
    path("", TemplateView.as_view(template_name="paslaugos/index.html")),
]
