from django.conf.urls import url
from arya_lib import views
#from django.conf.urls import patterns
urlpatterns = [
url(r'^$', views.login_page, name='login_page'),
url(r'home',views.home_page,name='home_page'),
]