from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name="register"),
    url(r'^create$', views.create, name="create"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^loginprocess$', views.loginprocess, name="loginprocess"),
    url(r'^$', views.index, name="index"),
]