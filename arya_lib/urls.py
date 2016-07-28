from django.conf.urls import url
from arya_lib import views
#from django.conf.urls import patterns
urlpatterns = [
url(r'^$', views.login, name='login'),
]