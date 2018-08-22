from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^account$', views.account, name='api.account'),
    url(r'^hosptital/$', views.patient_list, name="api.hosptial"),
    url(r'^hosptital/patient/(?P<pk>[0-9]+)$', views.patient_details, name="api.patient"),
]
