from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello_mundo, name='hello'),
    url(r'^recetas/(?P<pk>[0-9]+)/$', views.recet_detail),
    url(r'^recetas/new', views.new_recipe, name="new_recipe"),

]