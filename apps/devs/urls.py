from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register$', views.register, name="register"),
    url(r'^create$', views.create, name="create"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^loginprocess$', views.loginprocess, name="loginprocess"),
    url(r'^add_lang$', views.add_lang, name="add_lang"),
    url(r'^create_lang$', views.create_lang, name="create_lang"),
    url(r'^languages$', views.languages, name="languages"),
    url(r'^languageprocess$', views.languageprocess, name="languageprocess"),
    url(r'^add_framework$', views.add_framework, name="add_framework"),
    url(r'^create_framework$', views.create_framework, name="create_framework"),
    url(r'^frameworks$', views.frameworks, name="frameworks"),
    url(r'^frameworksprocess$', views.frameworksprocess, name="frameworksprocess"),
    url(r'^$', views.index, name="index"),
]