from django.conf.urls import url
from arya_lib import views
from django.conf.urls.defaults import patterns
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    )