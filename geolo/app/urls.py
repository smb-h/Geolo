from django.urls import include, path
from django.views.generic import TemplateView
from .views import home_view

app_name = 'App'

urlpatterns = [

    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about",),
    path("", home_view, name="home"),
  

]

