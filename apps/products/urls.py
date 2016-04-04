from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^', views.products, name='products'),
    url(r'^packaging/', views.packaging, name='packaging'),
    url(r'^automotive/', views.automotive, name='automotive'),
    url(r'^insulation/', views.insulation, name='insulation'),
]